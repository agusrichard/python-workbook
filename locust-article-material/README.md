# Load Testing using Locust.io

<br />

## List of Contents:
### 1. [Locust Documentation](https://docs.locust.io/en/stable/)

<br />

---

## Contents

## [Locust Documentation](https://docs.locust.io/en/stable/)

Locust is an easy to use, scriptable and scalable performance testing tool.

### Features:
- Write test scenarios in plain old Python <br />
  Locust runs every user inside its own greenlet (a lightweight process/coroutine).
- Distributed and scalable - supports hundreds of thousands of concurrent users <br />
  Possible to run load tests in distributed manner. . It is event-based (using gevent), which makes it possible for a single process to handle many thousands concurrent users.
- Web-based UI <br />
  Locust has a user friendly web interface that shows the progress of your test in real-time.
- Can test any system <br />
  Even though Locust primarily works with web sites/services, it can be used to test almost any system or protocol. Just write a client for what you want to test.
- Hackable <br />
  Locust is small and very flexible and we intend to keep it that way.
  
### Installation
- Install Python 3.6 or later
- Install Locust using pip: `pip install locust`
- Validate the installation using `locust -V`
- If we need some feature or fix not yet part of a release, we can use this to install <br />
  `pip3 install -e git://github.com/locustio/locust.git@master#egg=locus`
  
### Quick Start
locustfile.py

```python
import time
from locust_tests.locustfile import HttpUser, task, between


class QuickstartUser(HttpUser):
    wait_time = between(1, 2.5)

    @task
    def hello_world(self):
        self.client.get("/hello")
        self.client.get("/world")

    @task(3)
    def view_items(self):
        for item_id in range(10):
            self.client.get(f"/item?id={item_id}", name="/item")
            time.sleep(1)

    def on_start(self):
        self.client.post("/login", json={"username": "foo", "password": "bar"})
```

**Explanation:**
- We can import code just like any other python module
- Define a class for the simulated users. Which inherits HttpUser which gives us access to client attribute and let us to make http call.
- Our class defines a wait_time that will make the simulated users wait between 1 and 2.5 seconds after each task (see below) is executed.
- Methods decorated with @task are the core of your locust file. For every running user, Locust creates a greenlet (micro-thread), that will call those methods.
- Tasks are picked at random, but you can give them different weighting. The above configuration will make Locust three times more likely to pick view_items than hello_world.
- The self.client attribute makes it possible to make HTTP calls that will be logged by Locust.
- n the view_items task we load 10 different URLs by using a variable query parameter. In order to not get 10 separate entries in Locust’s statistics - since the stats is grouped on the URL
- Additionally we’ve declared an on_start method. A method with this name will be called for each simulated user when they start.
- The above code is in `locustfile.py`. To run it: `locust`.
- If the locust file is located somewhere else, we can specify this: `locust -f locust_files/my_locust_file.py`


### Writing a Locustfile
- User class <br />
  Locust will spawn one instance of the User class for each user that is being simulated.
  - `wait_time` <br />
    Is an optional attribute used to determine how long a simulated user should wait between executing tasks. If no `wait_time` is specified, a new task will be executed as soon as one finishes.
  - There are three built in wait+time functions:
    - `constant`: for a fixed amount of time
    - `between`: for a random time between a min and max value
    - `constant_pacing`: for an adaptive time that ensures the task runs (at most) once every X seconds
  - Snippet how to use `wait_time`:
    ```python
    from locust_tests.locustfile import User, task, between
    
    class MyUser(User):
        wait_time = between(0.5, 10)
    
        @task
        def my_task(self):
            print("executing my_task")
    ```
  - Snippet of how to declare custom wait_time:
    ```python
    class MyUser(User):
    last_wait_time = 0

    def wait_time(self):
        self.last_wait_time += 1
        return self.last_wait_time

    ...
    ```
  - `weight` <br />
    If more than one user class exists in the file, and no user classes are specified on the command line, Locust will spawn an equal number of each of the user classes.
  - For example we have WebUser and Mobile user, we can specify which of the user classes from the same locustfile using this command `locust -f locust_file.py WebUser MobileUser`
  - We can also specify it right away on the python file
    ```python
    class WebUser(User):
        weight = 3
        ...
    
    class MobileUser(User):
        weight = 1
        ...
    ```
  - The above code means, WebUser is three times more likely than mobile users
  - `host` <br />
    The host attribute is a URL prefix (i.e. “http://google.com”) to the host that is to be loaded.
  - `environment` <br />
    E.g. to stop the runner from a task method: `self.environment.runner.quit()`
  - If run on a standalone locust instance, this will stop the entire run. If run on worker node, it will stop that particular node.
  - `on_start` and `on_stop` methods <br />
    A User will call its on_start method when it starts running, and its on_stop method when it stops running. For a TaskSet, the on_start method is called when a simulated user starts executing that TaskSet, and on_stop is called when the simulated user stops executing that TaskSet
    
### Tasks
- When a load test is started, an instance of a User class will be created for each simulated user and they will start running within their own green thread. When these users run they pick tasks that they execute, sleep for awhile, and then pick a new task and so on.
- How to add tasks:
  - using `@task` decorator
    ```python
    from locust_tests.locustfile import User, task, constant
    
    class MyUser(User):
        wait_time = constant(1)
    
        @task(1)    # 1 is the weight for this task
        def my_task(self):
            print("User instance (%r) executing my_task" % self)
    ```
  - Using `tasks` attribute <br />
    If the tasks attribute is specified as a list, each time a task is to be performed, it will be randomly chosen from the tasks attribute.
    If however, tasks is a dict - with callables as keys and ints as values - the task that is to be executed will be chosen at random but with the int as ratio. So with a task that looks like this: `{my_task: 3, another_task: 1}`
    my_task would be 3 times more likely to be executed than another_task.

    ```python
    from locust_tests.locustfile import User, constant
    
    def my_task(user):
        pass
    
    class MyUser(User):
        tasks = [my_task]
        wait_time = constant(1)
    ```
- `@tag` decorator <br />
  By tagging tasks using the @tag decorator, you can be picky about what tasks are executed during the test using the --tags and --exclude-tags arguments.
  - Snippet
    ```python
    from locust_tests.locustfile import User, constant, task, tag
    
    class MyUser(User):
        wait_time = constant(1)
    
        @tag('tag1')
        @task
        def task1(self):
            pass
    
        @tag('tag1', 'tag2')
        @task
        def task2(self):
            pass
    
        @tag('tag3')
        @task
        def task3(self):
            pass
    
        @task
        def task4(self):
            pass
    ```
    - We run the test using `--tags tag1`, so only `task1` and `task2` will run
    - We can also use `--exlude-tags` to exclude some tasks
  
### Events
- `test_start` and `test_stop` <br />
  ```python
    from locust_tests.locustfile import events
    
    @events.test_start.add_listener
    def on_test_start(environment, **kwargs):
        print("A new test is starting")
    
    @events.test_stop.add_listener
    def on_test_stop(environment, **kwargs):
        print("A new test is ending")
    ```
  - When running Locust distributed the test_start and test_stop events will only be fired in the master node.
- `init`
  The init event is triggered at the beginning of each Locust process. This is especially useful in distributed mode where each worker process (not each user) needs a chance to do some initialization. For example, let’s say you have some global state that all users spawned from this process will need:
  ```python
  from locust_tests.locustfile import events
  from locust_tests.locustfile import MasterRunner
  
  @events.init.add_listener
  def on_locust_init(environment, **kwargs):
      if isinstance(environment.runner, MasterRunner):
          print("I'm on master node")
      else:
          print("I'm on a worker or standalone node")
  ```
  
### HttpUser

```python
from locust_tests.locustfile import HttpUser, task, between


class MyUser(HttpUser):
    wait_time = between(5, 15)

    @task(4)
    def index(self):
        self.client.get("/")

    @task(1)
    def about(self):
        self.client.get("/about/")
```
- `client` attribute / `HttpSession`
  - client is an instance of HttpSession. HttpSession is a subclass/wrapper for requests.Session, so its features are well documented and should be familiar to many. What HttpSession adds is mainly reporting of the request results into Locust (success/fail, response time, response length, name).
  - Just like requests.Session, it preserves cookies between requests so it can easily be used to log in to websites.
  ```python
    response = self.client.post("/login", {"username":"testuser", "password":"secret"})
    print("Response status code:", response.status_code)
    print("Response text:", response.text)
    response = self.client.get("/my-profile")
  ```
  - HttpSession catches any requests.RequestException thrown by Session (caused by connection errors, timeouts or similar), instead returning a dummy Response object with status_code set to 0 and content set to None
- Validating responses
  - Requests are considered successful if the HTTP response code is OK (<400),
  - Snippet
    ```python
    with self.client.get("/", catch_response=True) as response:
        if response.text != "Success":
            response.failure("Got wrong response")
        elif response.elapsed.total_seconds() > 0.5:
            response.failure("Request took too long")
    
    with self.client.get("/does_not_exist/", catch_response=True) as response:
        if response.status_code == 404:
            response.success()
    
    # We can throw the exception and catch it somewehere else
    from locust_tests.locustfile import RescheduleTask
    ...
    with self.client.get("/does_not_exist/", catch_response=True) as response:
        if response.status_code == 404:
            raise RescheduleTask()
    ```
- REST/JSON APIs
```python
from json import JSONDecodeError
...
with self.client.post("/", json={"foo": 42, "bar": None}, catch_response=True) as response:
    try:
        if response.json()["greeting"] != "hello":
            response.failure("Did not get expected value in greeting")
    except JSONDecodeError:
        response.failure("Response could not be decoded as JSON")
    except KeyError:
        response.failure("Response did not contain expected key 'greeting'")
```

- Grouping requests
```python
# Statistics for these requests will be grouped under: /blog/?id=[id]
for i in range(10):
    self.client.get("/blog?id=%i" % i, name="/blog?id=[id]")
```


### How to structure the test code
For small tests, keeping all of the test code in a single locustfile.py should work fine, but for larger test suites, you’ll probably want to split the code into multiple files and directories.
    
### Command Line Options
- `-f LOCUSTFILE`: The file where our tests reside
- Command Line can be converted to a configfile.
  ```editorconfig
  # master.conf in current directory
  locustfile = locust_files/my_locust_file.py
  headless = true
  master = true
  expect-workers = 5
  host = http://target-system
  users = 100
  spawn-rate = 10
  run-time = 10m
  ```
- Locust will look for ~/.locust.conf and ./locust.conf by default, and you can specify an additional file using the --config flag.

### Running Locust distributed
- Start one instance of Locust in master node using the `--master` flag.
- Master node is the instance that will be running the Locust's web interface and doesn't simulate any users itself.
- Start one or multiple workers using `--worker` flag and `--master-host`  (to specify the IP/hostname of the master node).
- It’s recommended that you start a number of simulated users that are greater than number of user classes * number of workers when running Locust distributed.
- Example:
  ```shell
  locust -f my_locustfile.py --master
  
  locust -f my_locustfile.py --worker --master-host=192.168.0.14
  ```

### Running Locust with Docker
- With Docker
  ```shell
  docker run -p 8089:8089 -v $PWD:/mnt/locust locustio/locust -f /mnt/locust/locustfile.py
  ```
- Using docker-compose
  ```
  version: '3'
  
  services:
    master:
      image: locustio/locust
      ports:
       - "8089:8089"
      volumes:
        - ./:/mnt/locust
      command: -f /mnt/locust/locustfile.py --master -H http://master:8089
    
    worker:
      image: locustio/locust
      volumes:
        - ./:/mnt/locust
      command: -f /mnt/locust/locustfile.py --worker --master-host master
  ```
- E.g to run 4 workers using docker-compose
  ```shell
  docker-compose up --scale worker=4
  ```
- Using docker image as a base image
  ```dockerfile
  FROM locustio/locust
  RUN pip3 install some-python-package
  ```
  
### Running Locust without the web UI
- We can do this using `--headless` flag with `-u` and `-r` (u for user and r for spawn rate)
  ```shell
  locust -f locust_files/my_locust_file.py --headless -u 1000 -r 100
  ```
- Setting time limit
  ```shell
  locust -f --headless -u 1000 -r 100 --run-time 1h30m
  ```
- Allow tasks to finish their iteration on shutdown. `--stop-timeout <seconds>`
  ```shell
  locust -f --headless -u 1000 -r 100 --run-time 1h30m --stop-timeout 99
  ```
- Controllin the exit ode of the Locust process
  ```python
  import logging
  from locust_tests.locustfile import events
  
  @events.quitting.add_listener
  def _(environment, **kw):
      if environment.stats.total.fail_ratio > 0.01:
          logging.error("Test failed due to failure ratio > 1%")
          environment.process_exit_code = 1
      elif environment.stats.total.avg_response_time > 200:
          logging.error("Test failed due to average response time ratio > 200 ms")
          environment.process_exit_code = 1
      elif environment.stats.total.get_response_time_percentile(0.95) > 800:
          logging.error("Test failed due to 95th percentile response time > 800 ms")
          environment.process_exit_code = 1
      else:
          environment.process_exit_code = 0
  ```

### Generating a custom load shape
- Sometimes a completely custom shaped load test is required that cannot be achieved by simply setting or changing the user count and spawn rate. For example, you might want to generate a load spike or ramp up and down at custom times.
- Define a class inheriting the LoadTestShape class in your locust file.
- In this class you define a tick() method that returns a tuple with the desired user count and spawn rate (or None to stop the test). Locust will call the tick() method approximately once per second.
- Example:
  ```python
  class MyCustomShape(LoadTestShape):
      time_limit = 600
      spawn_rate = 20
  
      def tick(self):
          run_time = self.get_run_time()
  
          if run_time < self.time_limit:
              # User count rounded to nearest hundred.
              user_count = round(run_time, -2)
              return (user_count, spawn_rate)
  
          return None
  ```

### Retrieve test statistics in CSV format
- Using Web UI, we can download the statistics
- With Locust flag:
  ```shell
  locust -f examples/basic.py --csv=example --headless -t10m
  ```
- The files will be named example_stats.csv, example_failures.csv and example_history.csv (when using --csv=example). The first two files will contain the stats and failures for the whole test run, with a row for every stats entry (URL endpoint) and an aggregated row. The example_history.csv will get new rows with the current (10 seconds sliding window) stats appended during the whole test run. By default only the Aggregate row is appended regularly to the history stats, but if Locust is started with the --csv-full-history flag, a row for each stats entry (and the Aggregate) is appended every time the stats are written (once every 2 seconds by default).
- In python file
  ```python

from locust_tests import locustfile
  locust.stats.CSV_STATS_INTERVAL_SEC = 5 # default is 1 second
  locust.stats.CSV_STATS_FLUSH_INTERVAL_SEC = 60 # Determines how often the data is flushed to disk, default is 10 seconds
  ```

### Extending Locust using event hooks

```python
from locust_tests.locustfile import events


@events.request.add_listener
def my_request_handler(request_type, name, response_time, response_length, response,
                       context, exception, **kwargs):
    if exception:
        print(f"Request to {name} failed with exception {exception}")
    else:
        print(f"Successfully made a request to: {name})
        print(f"The response was {response.text}")
```
- Request context
  ```python
  class MyUser(HttpUser):
      @task
      def t(self):
          self.client.post("/login", json={"username": "foo"}, context={"username": "foo"})
  
      @events.request.add_listener
      def on_request(context, **kwargs):
          print(context["username"])
  
  class MyUser(HttpUser):
      def context(self):
          return {"username": self.username}
  
      @task
      def t(self):
          self.username = "foo"
          self.client.post("/login", json={"username": self.username})
  
      @events.request.add_listener
      def on_request(context, **kwargs):
          print(context["username"])
  ```
- Adding web routes
  You should now be able to start locust and browse to http://127.0.0.1:8089/added_page
  ```python
  from locust_tests.locustfile import events
  
  @events.init.add_listener
  def on_locust_init(web_ui, **kw):
      @web_ui.app.route("/added_page")
      def my_added_page():
          return "Another page"
  ```
- Run a background greenlet <br />
  For example, you can monitor the fail ratio of your test and stop the run if it goes above some threshold:
  ```python
  from locust_tests.locustfile import events
  from locust_tests.locustfile import STATE_STOPPING, STATE_STOPPED, STATE_CLEANUP, WorkerRunner
  
  def checker(environment):
      while not environment.runner.state in [STATE_STOPPING, STATE_STOPPED, STATE_CLEANUP]:
          time.sleep(1)
          if environment.runner.stats.total.fail_ratio > 0.2:
              print(f"fail ratio was {environment.runner.stats.total.fail_ratio}, quitting")
              environment.runner.quit()
              return
  
  
  @events.init.add_listener
  def on_locust_init(environment, **_kwargs):
      # only run this on master & standalone
      if not isinstance(environment.runner, WorkerRunner):
          gevent.spawn(checker, environment)
  ```



<br />

---

## References:
- https://docs.locust.io/en/stable/