from datetime import datetime
from playwright.sync_api import Page
from utils.assertions import Assertions
from pages.base_page import BasePage
from utils.logger import get_logger

logger = get_logger(__name__)


class CreateOrderPage(BasePage):

    def __init__(self, page: Page):
        super().__init__(page)
        self.assertions = Assertions()

        # ORIGIN (STOP 1)
        self.origin = page.locator('//div[@id="stop-1_content"]')

        self.origin_location_name = page.locator('//input[@id="stop-1-content-location-name"]')
        self.origin_address_line1 = page.locator('//input[@id="stop-1-content-location-line1"]')
        self.origin_address_line2 = page.locator('//input[@id="stop-1-content-location-line2"]')
        self.origin_address_line3 = page.locator('//input[@id="stop-1-content-location-line3"]')
        self.origin_city = page.locator('//input[@id="stop-1-content-location-city"]')
        self.origin_state = page.locator('//span[@id="stop-1-content-location-state"]')
        self.origin_postal_code = page.locator('//input[@id="stop-1-content-location-postal-code"]')
        self.origin_reference_number = self.origin.get_by_label("Location Code")
        self.origin_contact_name = page.locator('//input[@id="stop-1-content-contact-contact-name"]')
        self.origin_contact_phone = page.locator('//input[@id="stop-1-content-contact-contact-phone"]')
        self.origin_contact_email = page.locator('//input[@id="stop-1-content-contact-contact-email"]')
        self.origin_contact_company = page.locator('//input[@id="stop-1-content-contact-contact-company"]')
        self.origin_internal_notes = page.locator('//textarea[@id="stop-1-content-internal-notes"]')
        self.origin_special_instructions = page.locator('//textarea[@id="stop-1-content-carrier-special-instructions"]')
        self.origin_earliest_pickup = page.locator("#stop-1-content-earliest-PICKUP")

        self.origin_appointment_required = self.origin.get_by_label("Appointment Required")
        self.origin_save_to_address_book = self.origin.get_by_label("Save to Address Book")
        self.origin_requested_date_lock = self.origin.get_by_label("Requested Date Lock")
        self.origin_requested_time_lock = self.origin.get_by_label("Requested Time Lock")

        # DESTINATION (STOP 2)
        self.destination = page.locator('//div[@id="stop-2_content"]')
        self.destination_location_name = page.locator('//input[@id="stop-2-content-location-name"]')
        self.destination_address_line1 = page.locator('//input[@id="stop-2-content-location-line1"]')
        self.destination_address_line2 = page.locator('//input[@id="stop-2-content-location-line2"]')
        self.destination_address_line3 = page.locator('//input[@id="stop-2-content-location-line3"]')
        self.destination_city = page.locator('//input[@id="stop-2-content-location-city"]')
        self.destination_state = page.locator('//span[@id="stop-2-content-location-state"]')
        self.destination_postal_code = page.locator('//input[@id="stop-2-content-location-postal-code"]')
        self.destination_reference_number = page.locator('//input[@id="stop-2-content-location-reference-number"]')
        self.destination_country = page.locator('//span[@id="stop-2-content-location-country"]')
        self.destination_contact_name = page.locator('//input[@id="stop-2-content-contact-contact-name"]')
        self.destination_contact_phone = page.locator('//input[@id="stop-2-content-contact-contact-phone"]')
        self.destination_contact_email = page.locator('//input[@id="stop-2-content-contact-contact-email"]')
        self.destination_contact_company = page.locator('//input[@id="stop-2-content-contact-contact-company"]')
        self.destination_internal_notes = page.locator('//textarea[@id="stop-2-content-internal-notes"]')
        self.destination_special_instructions = page.locator('//textarea[@id="stop-2-content-carrier-special-instructions"]')
        self.destination_dropoff_date = page.locator("#stop-2-content-earliest-DROP_OFF")

        self.destination_appointment_required = self.destination.get_by_label("Appointment Required")
        self.destination_save_to_address_book = self.destination.get_by_label("Save to Address Book")
        self.destination_requested_date_lock = self.destination.get_by_label("Requested Date Lock")
        self.destination_requested_time_lock = self.destination.get_by_label("Requested Time Lock")

        # LINE ITEM
        self.line_item = page.locator('//div[@id="line-item-num-1-content"]')
        self.description = page.locator('//input[@placeholder="Enter a description or select a product"]')
        self.handling = page.locator('//input[@placeholder="Handling"]')
        self.weight = page.locator('//input[@placeholder="Weight"]')
        self.length = page.locator('//input[@placeholder="Length"]')
        self.width = page.locator('//input[@placeholder="Width"]')
        self.height = page.locator('//input[@placeholder="Height"]')
        self.value = page.locator('//input[@value="$0.00" and @id="value-of-goods-0"]')
        self.density = page.locator('//input[@placeholder="Density"]')

        self.product_number = page.locator('//input[@id="product-number-0"]')
        self.nmfc_number = page.locator('//input[@id="nmfc-number-0"]')
        self.class_number = page.locator('//span[@id="freight-class-0"]')

        self.sales_order_number = page.locator('//input[contains(@id,"reference-number_") and contains(@id,"-value")]')

        # BASIC INFO
        self.basic_info = page.locator('//div[@class="p-card-content" and @data-pc-section="content"]').nth(1)
        self.direction = self.basic_info.locator("#direction")
        self.billing_terms = self.basic_info.locator("#billing-terms")

        # CREATE ORDER
        self.create_order_button = page.get_by_role("button", name="Create Order for JCB")
        self.success_message = page.get_by_text("Successfully saved order", exact=True)

    # ORIGIN DETAILS

    def enter_origin_details(self, origin_data):
        logger.info("Entering origin details")

        self.fill(self.origin_location_name, origin_data["location_name"])
        self.page.keyboard.press("Escape")

        self.fill(self.origin_address_line1, origin_data.get("address_line_1") or origin_data.get("address_line1", ""))
        self.page.keyboard.press("Escape")

        if origin_data.get("address_line_2") or origin_data.get("address_line2"):
            self.fill(self.origin_address_line2, origin_data.get("address_line_2") or origin_data.get("address_line2", ""))

        if origin_data.get("address_line_3") or origin_data.get("address_line3"):
            self.fill(self.origin_address_line3, origin_data.get("address_line_3") or origin_data.get("address_line3", ""))

        self.fill(self.origin_city, origin_data.get("city", ""))

        state = origin_data.get("state", "")
        if state:
            self.select_dropdown(self.origin_state, state)

        # POSTAL CODE
        self.fill(self.origin_postal_code, origin_data.get("postal_code", ""))

        # CONTACT DETAILS
        self.fill(self.origin_contact_name, origin_data.get("contact_name", ""))
        self.fill(self.origin_contact_phone, origin_data.get("contact_phone_number") or origin_data.get("contact_phone", ""))
        self.fill(self.origin_contact_email, origin_data.get("contact_email", ""))
        self.fill(self.origin_contact_company, origin_data.get("company_name") or origin_data.get("contact_company", ""))

        # NOTES
        self.fill(self.origin_internal_notes, origin_data.get("internal_notes", ""))
        self.fill(self.origin_special_instructions, origin_data.get("carrier_special_instructions", ""))

    def set_origin_toggles(self):
        self.check(self.origin_appointment_required)
        self.uncheck(self.origin_requested_date_lock)
        self.check(self.origin_requested_time_lock)
        logger.info("Origin details entered successfully")

    def _set_calendar_time(self, calendar, target_datetime):
        target_hour = target_datetime.strftime("%I")
        target_minute = target_datetime.strftime("%M")
        target_ampm = target_datetime.strftime("%p").lower()

        logger.info(
            f"Setting time to {target_hour}:{target_minute} {target_ampm.upper()}"
        )

        # SET HOUR
        hour_display = calendar.locator('[data-pc-section="hour"]')
        next_hour = calendar.get_by_role("button", name="Next Hour")

        for _ in range(12):
            current_hour = hour_display.inner_text().strip()
            if current_hour == target_hour or int(current_hour) == int(target_hour):
                break
            next_hour.click(force=True)

        # SET MINUTE
        minute_display = calendar.locator('[data-pc-section="minute"]')
        next_minute = calendar.get_by_role("button", name="Next Minute")

        for _ in range(12):
            current_minute = minute_display.inner_text().strip()
            if current_minute == target_minute or int(current_minute) == int(target_minute):
                break
            next_minute.click(force=True)

        # SET AM / PM
        ampm_display = calendar.locator('[data-pc-section="ampm"]')
        current_ampm = ampm_display.inner_text().strip().lower()

        if current_ampm != target_ampm:
            ampm_button = calendar.get_by_role("button", name=target_ampm)
            if ampm_button.is_visible():
                ampm_button.click(force=True)

        logger.info(
            f"Time selected: {target_hour}:{target_minute} {target_ampm.upper()}"
        )

    def set_pickup_datetime(self, pickup_datetime=None):
        if pickup_datetime is None:
            # Default to today at 04:00 PM
            pickup_datetime = datetime.now().replace(hour=16, minute=0, second=0, microsecond=0)
        elif isinstance(pickup_datetime, str):
            try:
                pickup_datetime = datetime.strptime(pickup_datetime, "%m/%d/%Y %I:%M %p")
            except Exception:
                pickup_datetime = datetime.now().replace(hour=16, minute=0, second=0, microsecond=0)

        logger.info(
            f"Setting pickup date/time: {pickup_datetime.strftime('%m/%d/%Y %I:%M %p')}"
        )

        # Open Requested Earliest Pickup
        self.click(self.origin_earliest_pickup)

        # Get visible calendar
        calendar = self.page.locator(".p-datepicker-panel:visible, .p-datepicker:visible, [role='dialog']:visible").last
        calendar.wait_for(state="visible")

        # Select today's date dynamically
        today_cell = calendar.locator(".p-datepicker-today, td.p-datepicker-today span, [data-pc-section='today']").first
        if today_cell.is_visible():
            self.click(today_cell)
        else:
            target_day = str(pickup_datetime.day)
            day_cell = calendar.locator(
                f'td:not(.p-datepicker-other-month) span:text-is("{target_day}"), '
                f'td:not(.p-datepicker-other-month) [data-pc-section="daycell"]:text-is("{target_day}")'
            ).first
            if not day_cell.is_visible():
                day_cell = calendar.locator("td:not(.p-datepicker-other-month) span").filter(has_text=target_day).first
            self.click(day_cell)

        # Set time dynamically
        self._set_calendar_time(calendar, pickup_datetime)
        self.page.keyboard.press("Escape")
        logger.info("Pickup date and time selected successfully")

    # DESTINATION DETAILS

    def enter_destination_details(self, destination_data):
        logger.info("Entering destination details")

        self.fill(self.destination_location_name, destination_data.get("location_name", ""))
        self.page.keyboard.press("Escape")

        self.fill(self.destination_address_line1, destination_data.get("address_line_1") or destination_data.get("address_line1", ""))
        self.page.keyboard.press("Escape")

        if destination_data.get("address_line_2") or destination_data.get("address_line2"):
            self.fill(self.destination_address_line2, destination_data.get("address_line_2") or destination_data.get("address_line2", ""))

        if destination_data.get("address_line_3") or destination_data.get("address_line3"):
            self.fill(self.destination_address_line3, destination_data.get("address_line_3") or destination_data.get("address_line3", ""))

        self.fill(self.destination_city, destination_data.get("city", ""))

        state = destination_data.get("state", "")
        if state:
            self.select_dropdown(self.destination_state, state)

        self.fill(self.destination_postal_code, destination_data.get("postal_code", ""))

        # CONTACT DETAILS
        self.fill(self.destination_contact_name, destination_data.get("contact_name", ""))
        self.fill(self.destination_contact_phone, destination_data.get("contact_phone_number") or destination_data.get("contact_phone", ""))
        self.fill(self.destination_contact_email, destination_data.get("contact_email", ""))
        self.fill(self.destination_contact_company, destination_data.get("company_name") or destination_data.get("contact_company", ""))

        # NOTES
        self.fill(self.destination_internal_notes, destination_data.get("internal_notes", ""))
        self.fill(self.destination_special_instructions, destination_data.get("carrier_special_instructions", ""))

    def assert_destination_toggles(self):
        self.destination_appointment_required.scroll_into_view_if_needed()
        self.check(self.destination_appointment_required)
        self.assertions.assert_checked(self.destination_appointment_required)

        self.destination_save_to_address_book.scroll_into_view_if_needed()
        self.check(self.destination_save_to_address_book)
        self.assertions.assert_checked(self.destination_save_to_address_book)

        self.destination_requested_date_lock.scroll_into_view_if_needed()
        self.check(self.destination_requested_date_lock)
        self.assertions.assert_checked(self.destination_requested_date_lock)

        self.destination_requested_time_lock.scroll_into_view_if_needed()
        self.check(self.destination_requested_time_lock)
        self.assertions.assert_checked(self.destination_requested_time_lock)

        logger.info("Destination details entered successfully")

    # LINE ITEM DETAILS

    def enter_line_item_details(self, line_item_data):
        logger.info("Entering line item details")

        self.fill(self.description, line_item_data["description"])
        self.page.keyboard.press("Escape")

        self.fill(self.handling, line_item_data["handling"])
        self.fill(self.weight, line_item_data["weight"])
        self.fill(self.length, line_item_data["length"])
        self.fill(self.width, line_item_data["width"])
        self.fill(self.height, line_item_data["height"])
        self.fill(self.value, line_item_data["value"])
        self.fill(self.density, line_item_data["density"])
        self.fill(self.sales_order_number, line_item_data["sales_order_number"])

        logger.info("Line item details entered successfully")

    # BASIC INFO

    def select_direction(self, basic_info=None):
        if isinstance(basic_info, dict):
            direction = basic_info.get("direction", "Inbound")
        elif isinstance(basic_info, str):
            direction = basic_info
        else:
            direction = "Inbound"
        self.select_dropdown(self.direction, direction)

    def select_billing_terms(self, basic_info):
        billing_terms = basic_info["billing_terms"]
        self.select_dropdown(self.billing_terms, billing_terms)

    # CREATE ORDER

    def click_create_order(self):
        logger.info("Clicking Create Order")
        self.click(self.create_order_button)

    def get_success_message(self):
        self.wait_for_visible(self.success_message)
        return self.get_text(self.success_message)