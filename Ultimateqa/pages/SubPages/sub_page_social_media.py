from playwright.sync_api import Page


class SubPageSocialMedia:
    def __init__(self, page: Page):
        self.page = page
        self.section = page.query_selector('.et_pb_row.et_pb_row_4')

