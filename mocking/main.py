from unittest import mock

# m = mock.Mock()

# m.foo.return_value = 1
# assert m.foo() == 1
# assert m.foo.called
# assert isinstance(m.bar, mock.Mock)
# assert isinstance(m(), mock.Mock)

# m.bar = 'bar'
# assert m.bar == 'bar'

# m.return_value = 'Sekar'
# assert m() == 'Sekar'

# m.side_effect = ['foo', 'bar', 'baz']
# assert m() == 'foo'
# assert m() == 'bar'
# assert m() == 'baz'

# try:
#     m()
# except StopIteration:
#     assert True
# else:
#     assert False

# m.side_effect = ValueError('foo')
# try:
#     m()
# except ValueError:
#     assert True
# else:
#     assert False

# m = mock.Mock()

# m()
# m()
# m.assert_called()
# try:
#     m.assert_called_once()
# except AssertionError:
#     assert True
# else:
#     assert False

m = mock.Mock()

m.side_effect = ValueError('foo')

try:
    m(1, foo='bar')
except ValueError:
    assert True
else:
    assert False

assert m.call_args_list == [mock.call(1, foo='bar')]

m.reset_mock()
assert m.call_args is None