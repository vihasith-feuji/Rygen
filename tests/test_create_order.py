import allure
import pytest
from pages.login_page import LoginPage
from pages.domain_page import DomainPage
from pages.order_page import OrderPage
from pages.create_order_page import CreateOrderPage
from config import BASE_URL, USERNAME, PASSWORD, DOMAIN
from utils.test_data_read import load_order_data
from utils.assertions import Assertions

# Load JSON test data
order_data = load_order_data()


@allure.epic("Rygen Order Management")
@allure.feature("Order Creation")
@allure.story("Create New JCB Order")
@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.parametrize("order", order_data["orders"])
def test_create_order(page, order):



    # 1: Login
    with allure.step("Step 1: Log in to Rygen application"):
        login_page = LoginPage(page)
        login_page.navigate(BASE_URL)
        login_page.login(USERNAME, PASSWORD)

    # 2: Domain Selection
    with allure.step(f"Step 2: Search and select domain '{DOMAIN}'"):
        domain_page = DomainPage(page)
        domain_page.search_domain(DOMAIN)
        domain_page.select_domain(DOMAIN)

    # 3: Navigate to New Order
    with allure.step("Step 3: Open Order menu and click New Order"):
        order_page = OrderPage(page)
        order_page.click_order()
        order_page.click_new_order()
        order_page.close_popup()

    create_order_page = CreateOrderPage(page)

    # 4: Pickup Date & Time
    with allure.step("Step 4: Set pickup date and time in calendar"):
        create_order_page.set_pickup_datetime()

    # 5: Origin Details
    with allure.step("Step 5: Enter Origin details"):
        create_order_page.enter_origin_details(order["origin"])
        create_order_page.set_origin_toggles()

    # 6: Destination Details
    with allure.step("Step 6: Enter Destination details"):
        create_order_page.enter_destination_details(order["destination"])
        create_order_page.assert_destination_toggles()

    # 7: Line Item Details
    with allure.step("Step 7: Enter Line Item product details"):
        assert order["line_item"]["description"], "Line item description is required"
        create_order_page.enter_line_item_details(order["line_item"])

    # 8: Basic Info
    with allure.step("Step 8: Select Direction and Billing Terms"):
        create_order_page.select_direction(order["basic_info"])
        create_order_page.select_billing_terms(order["basic_info"])

    # 9: Create Order & Verify Success
    with allure.step("Step 9: Click Create Order button and verify success message"):
        create_order_page.click_create_order()
        
        Assertions.assert_visible(create_order_page.success_message)
        Assertions.assert_contains_text(create_order_page.success_message, "Successfully saved order")
        
        message = create_order_page.get_success_message()
        assert message == "Successfully saved order", f"Expected 'Successfully saved order' but got '{message}'"
