import pytest
from src.pushover import Pushover

class TestPushover:
    def test_pushover_do_post(self):
        """
        test a correct push over rest
        """
        data = {
            'title': 'Test Notification Title',
            'message': 'Test Notification Message'
        }

        action = Pushover.do_post(data)

        assert action.request.method == 'POST'
        assert action.status_code == 200
        assert action.ok == True

    def test_pushover_do_post_wrong_data(self):
        """
        test a wrong pushover post without necessary data
        """
        data = {'wrong_data': 'Should not work'}

        action = Pushover.do_post(data)

        assert action.status_code == 400
        assert action.ok == False

    def test_pushover_do_post_wrong_data_typing(self):
        """
        test a wrong pushover post with data not as a dict
        """
        with pytest.raises(TypeError):
            data = 'not a dict'

            action = Pushover.do_post(data)

    def test_send_notification(self):
        """
        test a correct send notification
        """
        title = 'Test Send Notification Title'
        message = 'Test Send Notification Message'

        action = Pushover.send_notification(title, message)

        assert action == True
