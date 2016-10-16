class DisplayItem(object):
    def __init__(self, channel_id, channel_name, channel_url, channel_logo):
        self._channel_id = channel_id
        self._channel_name = channel_name
        self._channel_url = channel_url
        self._channel_logo = channel_logo

    @property
    def channel_id(self):
        return self._channel_id

    @property
    def channel_name(self):
        return self._channel_name

    @property
    def channel_url(self):
        return self._channel_url

    @property
    def channel_logo(self):
        return self._channel_logo
