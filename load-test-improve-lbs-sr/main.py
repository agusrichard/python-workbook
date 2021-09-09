from locust import HttpUser, task, between


class RunLoadTest(HttpUser):
    wait_time = between(1, 2)

    @task(1)
    def get_all_sr(self):
        request_body = {
            "action": "GET_ALL_SERVICE_REQUEST",
            "query": {
                "Skip": 0,
                "Take": 10,
                "Filters": [],
                "Orders": []
            }
        }
        request_headers = {
            "email": "Agus.Richard-EXT@xapiens.id",
            "location": '[{"id":6,"description":"Kariangau"},{"id":7,"description":"Sorong"}]'
        }
        response = self.client.post('/settlement?skip=0&take=100&filter=[]', name="/get-all-sr/not-concurrent", json=request_body, headers=request_headers)

    @task(1)
    def get_all_sr_concurrent(self):
        request_body = {
            "action": "GET_ALL_SERVICE_REQUEST_CONCURRENT",
            "query": {
                "Skip": 0,
                "Take": 10,
                "Filters": [],
                "Orders": []
            }
        }
        request_headers = {
            "email": "Agus.Richard-EXT@xapiens.id",
            "location": '[{"id":6,"description":"Kariangau"},{"id":7,"description":"Sorong"}]'
        }
        response = self.client.post('/settlement?skip=0&take=100&filter=[]', name="/get-all-sr/concurrent", json=request_body, headers=request_headers)

    @task(2)
    def get_sr_detail(self):
        request_body = {
            "action":"GET_DETAIL_SERVICE_REQUEST",
            "data": {
                    "sr_no": "SR0062108035"
            }
        }

        request_headers = {
            "email": "Agus.Richard-EXT@xapiens.id",
            "location": '[{"id":6,"description":"Kariangau"},{"id":7,"description":"Sorong"}]'
        }
        response = self.client.post('/settlement', name="/get-sr-detail/not-concurrent",
                                    json=request_body, headers=request_headers)

    @task(2)
    def get_sr_detail_concurrent(self):
        request_body = {
            "action":"GET_DETAIL_SERVICE_REQUEST_CONCURRENT",
            "data": {
                    "sr_no": "SR0062108035"
            }
        }

        request_headers = {
            "email": "Agus.Richard-EXT@xapiens.id",
            "location": '[{"id":6,"description":"Kariangau"},{"id":7,"description":"Sorong"}]'
        }
        response = self.client.post('/settlement', name="/get-sr-detail/concurrent",
                                    json=request_body, headers=request_headers)