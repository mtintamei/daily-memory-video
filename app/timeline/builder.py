class TimelineBuilder:

    def build(self, media_items):

        return sorted(
            media_items,
            key=lambda item: (
                item.capture_time is None,
                item.capture_time
            )
        )