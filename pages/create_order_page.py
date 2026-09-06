from datetime import datetime

from playwright.sync_api import Page, expect

from pages.base_page import BasePage


class CreateOrderPage(BasePage):

    def __init__(self, page: Page):
        super().__init__(page)

        # =================================================
        # SELECT CLIENT POPUP
        # =================================================

        self.select_client_popup = page.locator(".p-dialog").filter(has_text="Select Client")

        self.cancel_button = self.select_client_popup.get_by_role("button",name="Cancel")

        # =================================================
        # NEW ORDER
        # =================================================

        self.new_order_button = page.get_by_text("New Order",exact=True)

        # =================================================
        # DATE PICKER BUTTONS
        # =================================================

        self.date_picker_buttons = page.get_by_role("button",name="Choose Date")

        # =================================================
        # STOP 1 - LOCATION
        # =================================================

        self.location_name_input = page.locator("#stop-1-content-location-name")

        self.address_line1_input = page.locator("#stop-1-content-location-line1")

        self.address_line2_input = page.locator("#stop-1-content-location-line2")

        self.address_line3_input = page.locator("#stop-1-content-location-line3")

        self.city_input = page.locator("#stop-1-content-location-city")

        self.state_input = page.locator("#stop-1-content-location-state")

        self.postal_code_input = page.locator("#stop-1-content-location-postal-code")

        self.country_input = page.locator("#stop-1-content-location-country")

        self.reference_number_input = page.locator("#stop-1-content-location-reference-number")

        # =================================================
        # STOP 1 - CONTACT
        # =================================================

        self.contact_name_input = page.locator("#stop-1-content-contact-contact-name")

        self.contact_phone_input = page.locator("#stop-1-content-contact-contact-phone")

        self.contact_email_input = page.locator("#stop-1-content-contact-contact-email")

        self.contact_company_input = page.locator("#stop-1-content-contact-contact-company")

        # =================================================
        # STOP 1 - NOTES
        # =================================================

        self.internal_notes_input = page.locator("#stop-1-content-internal-notes")

        self.carrier_special_instructions_input = page.locator("#stop-1-content-carrier-special-instructions")

        self.stop1_timezone_dropdown = page.locator("#stop-1-content-tz-PICKUP")

        self.stop1_appointment_required = page.locator(
            "#stop-1-content-appointment-required"
        )

        self.stop1_save_to_address_book = page.locator(
            "#stop-1-content-save-to-address-book"
        )

        self.stop1_requested_date_lock = page.locator(
            "#stop-1-content-requested-date-lock"
        )

        self.stop1_requested_time_lock = page.locator(
            "#stop-1-content-requested-time-lock"
        )

        # =================================================
        # STOP 2 - LOCATION
        # =================================================

        self.stop2_location_name_input = page.locator(
            "#stop-2-content-location-name"
        )

        self.stop2_address_line1_input = page.locator(
            "#stop-2-content-location-line1"
        )

        self.stop2_address_line2_input = page.locator(
            "#stop-2-content-location-line2"
        )

        self.stop2_address_line3_input = page.locator(
            "#stop-2-content-location-line3"
        )

        self.stop2_city_input = page.locator(
            "#stop-2-content-location-city"
        )

        self.stop2_state_input = page.locator(
            "#stop-2-content-location-state"
        )

        self.stop2_postal_code_input = page.locator(
            "#stop-2-content-location-postal-code"
        )

        self.stop2_country_input = page.locator(
            "#stop-2-content-location-country"
        )

        self.stop2_location_code_input = page.locator(
            "#stop-2-content-location-reference-number"
        )

        self.stop2_location_group_input = page.locator(
            "#stop-2-content-location-group"
        )

        # =================================================
        # STOP 2 - CONTACT
        # =================================================

        self.stop2_contact_name_input = page.locator(
            "#stop-2-content-contact-contact-name"
        )

        self.stop2_contact_phone_input = page.locator(
            "#stop-2-content-contact-contact-phone"
        )

        self.stop2_contact_email_input = page.locator(
            "#stop-2-content-contact-contact-email"
        )

        self.stop2_contact_company_input = page.locator(
            "#stop-2-content-contact-contact-company"
        )

        # =================================================
        # STOP 2 - NOTES
        # =================================================

        self.stop2_internal_notes_input = page.locator(
            "#stop-2-content-internal-notes"
        )

        self.stop2_carrier_special_instructions_input = page.locator(
            "#stop-2-content-carrier-special-instructions"
        )

        self.stop2_timezone_dropdown = page.locator(
            "#stop-2-content-tz-DROP_OFF"
        )

        self.stop2_appointment_required = page.locator(
            "#stop-2-content-appointment-required"
        )

        self.stop2_save_to_address_book = page.locator(
            "#stop-2-content-save-to-address-book"
        )

        self.stop2_requested_date_lock = page.locator(
            "#stop-2-content-requested-date-lock"
        )

        self.stop2_requested_time_lock = page.locator(
            "#stop-2-content-requested-time-lock"
        )

        # =================================================
        # LINE ITEM / PRODUCT
        # =================================================

        self.product_description_input = page.locator(
            "#description-0"
        )

        self.handling_input = page.locator(
            "#handling-0"
        )

        self.weight_input = page.locator(
            "#weight-0"
        )

        self.length_input = page.locator(
            "#dims-0-length"
        )

        self.width_input = page.locator(
            "#dims-0-width"
        )

        self.height_input = page.locator(
            "#dims-0-height"
        )

        self.packaging_quantity_input = page.locator(
            "#packaging-quantity-0"
        )

        self.nmfc_number_input = page.locator(
            "#nmfc-number-0"
        )

        self.freight_class_dropdown = page.locator(
            "#freight-class-0"
        )

        self.linear_feet_input = page.locator(
            "#linear-feet-0 input"
        )

        self.product_number_input = page.locator(
            "#product-number-0"
        )

        self.density_input = page.locator(
            "#density-0"
        )

        self.value_of_goods_input = page.locator(
            "#value-of-goods-0"
        )

        self.turnable_switch = page.locator(
            "#turnable-0"
        )

        self.stackable_switch = page.locator(
            "#stackable-0"
        )

        self.hazardous_switch = page.locator(
            "#hazmat-0"
        )

        self.refrigerated_switch = page.locator(
            "#refrigerated-0"
        )

        self.save_product_switch = page.locator(
            "#save-product-0"
        )

        self.sales_order_number_input = page.locator(
            "#reference-number_2-value"
        )

        # =================================================
        # BASIC INFORMATION
        # =================================================

        self.direction_dropdown = page.locator(
            "#direction"
        )

        self.billing_terms_dropdown = page.locator(
            "#billing-terms"
        )

        self.requested_mode_dropdown = page.locator(
            "#requested-mode"
        )

        self.equipment_type_dropdown = page.locator(
            "#equipment-type"
        )

        self.basic_internal_notes_input = page.locator(
            "#internal-notes"
        )

        self.basic_carrier_notes_input = page.locator(
            "#carrier-notes"
        )

        # =================================================
        # SUBMIT / CREATE ORDER
        # =================================================

        self.create_order_button = page.locator("button").filter(
            has_text="Create Order"
        )

        # =================================================
        # ORDER DETAILS / STATUS
        # =================================================

        self.pending_status = page.locator("//div[text()='Pending']")

    # =====================================================
    # SELECT CLIENT POPUP
    # =====================================================

    def close_select_client_popup(self):

        expect(
            self.cancel_button
        ).to_be_visible(timeout=15000)

        self.cancel_button.click()

    # =====================================================
    # NEW ORDER
    # =====================================================

    def click_new_order(self):

        expect(
            self.new_order_button
        ).to_be_visible(timeout=15000)

        self.new_order_button.click()

    # =====================================================
    # STOP 1 - LOCATION
    # =====================================================

    def enter_location_name(self, value):

        self.location_name_input.wait_for(
            state="visible",
            timeout=30000
        )

        self.location_name_input.fill(value)

    def enter_address_line1(self, value):
        self.address_line1_input.fill(value)

    def enter_address_line2(self, value):
        if value:
            self.address_line2_input.fill(value)

    def enter_address_line3(self, value):
        if value:
            self.address_line3_input.fill(value)

    def enter_city(self, value):
        self.city_input.fill(value)

    def enter_state(self, value):

        self.state_input.click()

        option = self.page.get_by_role(
            "option",
            name=value,
            exact=True
        )

        expect(option).to_be_visible(timeout=10000)

        option.click()

    def enter_postal_code(self, value):
        self.postal_code_input.fill(value)

    def enter_country(self, value):
        if not value:
            return
        self.country_input.click()
        option = self.page.locator(".p-select-overlay, .p-dropdown-panel").get_by_role(
            "option",
            name=value,
            exact=True
        )
        expect(option).to_be_visible(timeout=10000)
        option.click()

    def enter_reference_number(self, value):
        if value:
            self.reference_number_input.fill(value)

    # =====================================================
    # STOP 1 - CONTACT
    # =====================================================

    def enter_contact_name(self, value):
        self.contact_name_input.fill(value)

    def enter_contact_phone(self, value):
        self.contact_phone_input.fill(value)

    def enter_contact_email(self, value):
        self.contact_email_input.fill(value)

    def enter_contact_company(self, value):
        self.contact_company_input.fill(value)

    # =====================================================
    # STOP 1 - NOTES
    # =====================================================

    def enter_internal_notes(self, value):
        if value:
            self.internal_notes_input.fill(value)

    def enter_carrier_special_instructions(self, value):
        if value:
            self.carrier_special_instructions_input.fill(value)

    # =====================================================
    # DATE PICKER HELPER
    # =====================================================

    def _select_date_time(self, button_index, value):

        if not value:
            return

        # ---------------------------------------------
        # Convert JSON date/time
        # ---------------------------------------------

        date_value = datetime.strptime(
            value,
            "%m/%d/%Y %I:%M %p"
        )

        day = str(date_value.day)
        hour = date_value.strftime("%I")
        minute = date_value.strftime("%M")
        am_pm = date_value.strftime("%p").lower()


        closing_panel = self.page.locator(
            ".p-datepicker-panel.p-anchored-overlay-leave-active"
        )

        if closing_panel.count() > 0:
            closing_panel.first.wait_for(
                state="hidden",
                timeout=5000
            )

        # ---------------------------------------------
        # Open calendar
        # ---------------------------------------------

        self.date_picker_buttons.nth(button_index).click()

        # ---------------------------------------------
        # Calendar dialog
        #
        # Exclude any panel still mid-close-animation so we
        # never match two "Choose Date" dialogs at once.
        # ---------------------------------------------

        dialog = self.page.locator(
            '[role="dialog"][aria-label="Choose Date"]'
            ":not(.p-anchored-overlay-leave-active)"
        )

        expect(dialog).to_be_visible(
            timeout=10000
        )

        # ---------------------------------------------
        # Select day
        #
        # Gridcell is much safer than:
        # get_by_text("5")
        # ---------------------------------------------

        dialog.get_by_role(
            "gridcell",
            name=day,
            exact=True
        ).click()

        # ---------------------------------------------
        # Set AM / PM
        # ---------------------------------------------

        time_picker = dialog.locator(".p-datepicker-time-picker")
        current_ampm = "am" if "am" in time_picker.inner_text().lower() else "pm"
        if current_ampm != am_pm:
            dialog.locator(".p-datepicker-time-picker button").last.click()

        # ---------------------------------------------
        # Set hour
        #
        # The picker has:
        # Previous Hour
        # Next Hour
        #
        # We start from the currently displayed hour
        # and click "Next Hour" until it matches.
        # (Removed the earlier no-op check block that
        # never advanced anything.)
        # ---------------------------------------------

        max_attempts = 24

        for _ in range(max_attempts):

            current = dialog.get_by_text(
                hour,
                exact=True
            )

            if current.count() > 0 and current.first.is_visible():
                break

            dialog.get_by_role(
                "button",
                name="Next Hour",
                exact=True
            ).click()

        # ---------------------------------------------
        # Set minute
        # ---------------------------------------------

        for _ in range(60):

            current_minute = dialog.get_by_text(
                minute,
                exact=True
            )

            if (
                current_minute.count() > 0
                and current_minute.first.is_visible()
            ):
                break

            dialog.get_by_role(
                "button",
                name="Next Minute",
                exact=True
            ).click()

        # ---------------------------------------------
        # Close picker
        # ---------------------------------------------

        self.page.keyboard.press("Escape")

    # =====================================================
    # STOP 1 - EARLIEST PICKUP
    # =====================================================

    def enter_stop1_requested_earliest_pickup(self, value):

        self._select_date_time(
            0,
            value
        )

    # =====================================================
    # STOP 1 - LATEST PICKUP
    # =====================================================

    def enter_stop1_requested_latest_pickup(self, value):

        self._select_date_time(
            1,
            value
        )

    # =====================================================
    # STOP 1 - TIMEZONE & TOGGLES
    # =====================================================

    def select_stop1_timezone(self, value):
        if not value:
            return
        self.stop1_timezone_dropdown.click()
        option = self.page.locator(".p-select-overlay, .p-dropdown-panel").get_by_role(
            "option",
            name=value,
            exact=True
        )
        expect(option).to_be_visible(timeout=10000)
        option.click()

    def set_stop1_toggles(self, appointment_required=None, save_to_address_book=None, requested_date_lock=None, requested_time_lock=None):
        if appointment_required is not None:
            self.stop1_appointment_required.set_checked(bool(appointment_required), force=True)
        if save_to_address_book is not None:
            self.stop1_save_to_address_book.set_checked(bool(save_to_address_book), force=True)
        if requested_date_lock is not None:
            self.stop1_requested_date_lock.set_checked(bool(requested_date_lock), force=True)
        if requested_time_lock is not None:
            self.stop1_requested_time_lock.set_checked(bool(requested_time_lock), force=True)

    # =====================================================
    # STOP 2 - LOCATION
    # =====================================================

    def enter_stop2_location_name(self, value):

        self.stop2_location_name_input.wait_for(
            state="visible",
            timeout=30000
        )

        self.stop2_location_name_input.fill(value)

    def enter_stop2_address_line1(self, value):
        self.stop2_address_line1_input.fill(value)

    def enter_stop2_address_line2(self, value):
        if value:
            self.stop2_address_line2_input.fill(value)

    def enter_stop2_address_line3(self, value):
        if value:
            self.stop2_address_line3_input.fill(value)

    def enter_stop2_city(self, value):
        self.stop2_city_input.fill(value)

    def enter_stop2_state(self, value):

        self.stop2_state_input.click()

        option = self.page.get_by_role(
            "option",
            name=value,
            exact=True
        )

        expect(option).to_be_visible(timeout=10000)

        option.click()

    def enter_stop2_postal_code(self, value):
        self.stop2_postal_code_input.fill(value)

    def enter_stop2_country(self, value):

        if not value:
            return

        self.stop2_country_input.click()

        option = self.page.get_by_role(
            "option",
            name=value,
            exact=True
        )

        expect(option).to_be_visible(timeout=10000)

        option.click()

    def enter_stop2_location_code(self, value):

        if value:
            self.stop2_location_code_input.fill(value)

    def enter_stop2_location_group(self, value):

        if value:
            self.stop2_location_group_input.fill(value)

    # =====================================================
    # STOP 2 - CONTACT
    # =====================================================

    def enter_stop2_contact_name(self, value):
        self.stop2_contact_name_input.fill(value)

    def enter_stop2_contact_phone(self, value):
        self.stop2_contact_phone_input.fill(value)

    def enter_stop2_contact_email(self, value):
        self.stop2_contact_email_input.fill(value)

    def enter_stop2_contact_company(self, value):
        self.stop2_contact_company_input.fill(value)

    # =====================================================
    # STOP 2 - EARLIEST DROPOFF
    # =====================================================

    def enter_stop2_requested_earliest_dropoff(self, value):

        self._select_date_time(
            2,
            value
        )

    # =====================================================
    # STOP 2 - LATEST DROPOFF
    # =====================================================

    def enter_stop2_requested_latest_dropoff(self, value):

        self._select_date_time(
            3,
            value
        )

    # =====================================================
    # STOP 2 - TIMEZONE & TOGGLES
    # =====================================================

    def select_stop2_timezone(self, value):
        if not value:
            return
        self.stop2_timezone_dropdown.click()
        option = self.page.locator(".p-select-overlay, .p-dropdown-panel").get_by_role(
            "option",
            name=value,
            exact=True
        )
        expect(option).to_be_visible(timeout=10000)
        option.click()

    def set_stop2_toggles(self, appointment_required=None, save_to_address_book=None, requested_date_lock=None, requested_time_lock=None):
        if appointment_required is not None:
            self.stop2_appointment_required.set_checked(bool(appointment_required), force=True)
        if save_to_address_book is not None:
            self.stop2_save_to_address_book.set_checked(bool(save_to_address_book), force=True)
        if requested_date_lock is not None:
            self.stop2_requested_date_lock.set_checked(bool(requested_date_lock), force=True)
        if requested_time_lock is not None:
            self.stop2_requested_time_lock.set_checked(bool(requested_time_lock), force=True)

    # =====================================================
    # STOP 2 - NOTES
    # =====================================================

    def enter_stop2_internal_notes(self, value):

        if value:
            self.stop2_internal_notes_input.fill(value)

    def enter_stop2_carrier_special_instructions(self, value):

        if value:
            self.stop2_carrier_special_instructions_input.fill(value)

    # =====================================================
    # LINE ITEM / PRODUCT
    # =====================================================

    def enter_product_description(self, value):
        if value:
            self.product_description_input.wait_for(
                state="visible",
                timeout=30000
            )
            self.product_description_input.fill(value)
            self.page.keyboard.press("Escape")

    def enter_handling(self, value):
        if value is not None and value != "":
            self.handling_input.fill(str(value))

    def enter_weight(self, value):
        if value is not None and value != "":
            self.weight_input.fill(str(value))

    def enter_length(self, value):
        if value is not None and value != "":
            self.length_input.fill(str(value))

    def enter_width(self, value):
        if value is not None and value != "":
            self.width_input.fill(str(value))

    def enter_height(self, value):
        if value is not None and value != "":
            self.height_input.fill(str(value))

    def enter_packaging(self, value):
        if value is not None and value != "":
            self.packaging_quantity_input.fill(str(value))

    def enter_nmfc_number(self, value):
        if value:
            self.nmfc_number_input.fill(str(value))

    def enter_product_number(self, value):
        if value:
            self.product_number_input.fill(str(value))

    def enter_density(self, value):
        if value is not None and value != "":
            self.density_input.fill(str(value))

    def enter_value_of_goods(self, value):
        if value is not None and value != "":
            self.value_of_goods_input.fill(str(value))

    def select_freight_class(self, value):
        if not value:
            return
        self.freight_class_dropdown.click()
        option = self.page.locator(".p-select-overlay, .p-dropdown-panel").get_by_role(
            "option",
            name=str(value),
            exact=True
        )
        expect(option).to_be_visible(timeout=10000)
        option.click()

    def enter_linear_feet(self, value):
        if value is not None and value != "":
            self.linear_feet_input.fill(str(value))

    def enter_sales_order_number(self, value):
        if value:
            self.sales_order_number_input.fill(str(value))

    def set_product_toggles(self, turnable=None, stackable=None, hazardous=None, refrigerated=None, save_to_product_list=None):
        if turnable is not None:
            self.turnable_switch.set_checked(bool(turnable), force=True)
        if stackable is not None:
            self.stackable_switch.set_checked(bool(stackable), force=True)
        if hazardous is not None:
            self.hazardous_switch.set_checked(bool(hazardous), force=True)
        if refrigerated is not None:
            self.refrigerated_switch.set_checked(bool(refrigerated), force=True)
        if save_to_product_list is not None:
            self.save_product_switch.set_checked(bool(save_to_product_list), force=True)

    # =====================================================
    # BASIC INFORMATION
    # =====================================================

    def select_direction(self, value):
        if not value:
            return
        self.direction_dropdown.click()
        option = self.page.locator(".p-select-overlay, .p-dropdown-panel").get_by_role(
            "option",
            name=value,
            exact=True
        )
        expect(option).to_be_visible(timeout=10000)
        option.click()

    def select_billing_terms(self, value):
        if not value:
            return
        self.billing_terms_dropdown.click()
        option = self.page.locator(".p-select-overlay, .p-dropdown-panel").get_by_role(
            "option",
            name=value,
            exact=True
        )
        expect(option).to_be_visible(timeout=10000)
        option.click()

    def select_requested_mode(self, value):
        if not value:
            return
        self.requested_mode_dropdown.click()
        option = self.page.locator(".p-select-overlay, .p-dropdown-panel").get_by_role(
            "option",
            name=value,
            exact=True
        )
        expect(option).to_be_visible(timeout=10000)
        option.click()

    def select_equipment_type(self, value):
        if not value:
            return
        self.equipment_type_dropdown.click()
        option = self.page.locator(".p-select-overlay, .p-dropdown-panel").get_by_role(
            "option",
            name=value,
            exact=True
        )
        expect(option).to_be_visible(timeout=10000)
        option.click()

    def enter_basic_internal_notes(self, value):
        if value:
            self.basic_internal_notes_input.fill(value)

    def enter_basic_carrier_notes(self, value):
        if value:
            self.basic_carrier_notes_input.fill(value)

    # =====================================================
    # SUBMIT / CREATE ORDER
    # =====================================================

    def click_create_order(self):
        expect(self.create_order_button.first).to_be_visible(timeout=15000)
        self.create_order_button.first.click()

    def verify_order_pending(self, timeout=30000):
        expect(self.pending_status).to_be_visible(timeout=timeout)