from slackclient import SlackClient


def send_slack(username, channel, text, icon_emoji=None):
    """
    Send slack message.
    """
    try:
        SLACK_TOKEN = configuration.get('slack', 'default_slack_token')
        assert SLACK_TOKEN
    except AssertionError:
        raise AirflowException('default_slack_token must be set in '
                               'airflow.cfg to use Slack retry and failure '
                               'notifications.')
    sc = SlackClient(SLACK_TOKEN)
    return sc.api_call('chat.postMessage', channel=channel, text=text,
                       username=username, icon_emoji=icon_emoji)
