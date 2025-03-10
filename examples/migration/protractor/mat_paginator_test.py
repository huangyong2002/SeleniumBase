from seleniumbase import BaseCase


class AngularMaterialPaginatorTests(BaseCase):
    def test_pagination(self):
        self.open("https://material.angular.io/components/paginator/examples")
        # Set pagination to 5 items per page
        self.click("mat-select > div")
        self.click("#mat-option-0")
        # Verify navigation to the next page
        self.click('button[aria-label="Next page"]')
        self.assert_exact_text(
            "Page 2 of 10", ".mat-mdc-paginator-range-label"
        )
        # Verify navigation to the previous page
        self.click('button[aria-label="Previous page"]')
        self.assert_exact_text(
            "Page 1 of 10", ".mat-mdc-paginator-range-label"
        )
        # Set pagination to 10 items per page
        self.click("mat-select > div")
        self.click("#mat-option-1")
        # Verify page with correct number of pages
        self.assert_exact_text("Page 1 of 5", ".mat-mdc-paginator-range-label")
