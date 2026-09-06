import allure
from playwright.sync_api import Page

from pages.login_page import LoginPage
from pages.domain_page import DomainPage
from pages.order_page import OrderPage
from pages.create_order_page import CreateOrderPage
from config import BASE_URL, USERNAME, PASSWORD


@allure.epic("Rygen Order Management")
@allure.feature("Order Creation")
@allure.story("Create New JCB Order & Verify Pending Status")
@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Create Order and Verify Pending Status")
@allure.description(
    "End-to-end automated test that logs into Rygen, selects the JCB domain, "
    "fills Stop 1 (Origin), Stop 2 (Destination), Line Item (Product), and Basic Information, "
    "submits the order, and verifies the order status reaches 'Pending'."
)
def test_create_order(
    page: Page,
    login_page: LoginPage,
    domain_page: DomainPage,
    order_page: OrderPage,
    create_order_page: CreateOrderPage,
    order_test_data: dict,
):
    data = order_test_data

    # =========================================================================
    # STEP 1: LOGIN
    # =========================================================================
    with allure.step("/nStep 1: Log in to Rygen application"):
        print("[Step 1/9] Logging in to Rygen...", flush=True)
        login_page.navigate(BASE_URL)
        login_page.login(USERNAME, PASSWORD)
        print("  -> Login successful.", flush=True)

    # =========================================================================
    # STEP 2: SELECT DOMAIN
    # =========================================================================
    domain_name = data["order"]["domain"]
    with allure.step(f"Step 2: Search and select domain '{domain_name}'"):
        print(f"[Step 2/9] Selecting domain: {domain_name}...", flush=True)
        domain_page.search_domain(domain_name)
        domain_page.select_jcb()
        print("  -> Domain selected.", flush=True)

    # =========================================================================
    # STEP 3: NAVIGATE TO ORDER ENTRY
    # =========================================================================
    with allure.step("Step 3: Open Order entry and start New Order"):
        print("[Step 3/9] Navigating to Order entry page...", flush=True)
        order_page.click_order()
        order_page.click_new_order()

        # Close client popup & initiate new order form
        create_order_page.close_select_client_popup()
        create_order_page.click_new_order()
        print("  -> Order creation form opened.", flush=True)

    # =========================================================================
    # STEP 4: FILL STOP 1 (ORIGIN)
    # =========================================================================
    stop1 = data["order"]["stop1"]
    with allure.step("Step 4: Fill Stop 1 (Origin) details"):
        print("[Step 4/9] Filling Stop 1 (Origin) details...", flush=True)

        # Location
        create_order_page.enter_location_name(stop1["location_name"])
        create_order_page.enter_address_line1(stop1["address_line1"])
        create_order_page.enter_address_line2(stop1["address_line2"])
        create_order_page.enter_address_line3(stop1["address_line3"])
        create_order_page.enter_city(stop1["city"])
        create_order_page.enter_state(stop1["state"])
        create_order_page.enter_postal_code(stop1["postal_code"])

        if stop1.get("country"):
            create_order_page.enter_country(stop1["country"])

        create_order_page.enter_reference_number(stop1["reference_number"])

        # Contact
        create_order_page.enter_contact_name(stop1["contact_name"])
        create_order_page.enter_contact_phone(stop1["contact_phone"])
        create_order_page.enter_contact_email(stop1["contact_email"])
        create_order_page.enter_contact_company(stop1["contact_company"])

        # Dates & Timezone
        create_order_page.enter_stop1_requested_earliest_pickup(stop1["requested_earliest_pickup"])
        create_order_page.enter_stop1_requested_latest_pickup(stop1["requested_latest_pickup"])

        if stop1.get("timezone"):
            create_order_page.select_stop1_timezone(stop1["timezone"])

        # Toggles & Notes
        create_order_page.set_stop1_toggles(
            appointment_required=stop1.get("appointment_required"),
            save_to_address_book=stop1.get("save_to_address_book"),
            requested_date_lock=stop1.get("requested_date_lock"),
            requested_time_lock=stop1.get("requested_time_lock"),
        )
        create_order_page.enter_internal_notes(stop1["internal_notes"])
        create_order_page.enter_carrier_special_instructions(stop1["carrier_special_instructions"])
        print("  -> Stop 1 completed.", flush=True)

    # =========================================================================
    # STEP 5: FILL STOP 2 (DESTINATION)
    # =========================================================================
    stop2 = data["order"]["stop2"]
    with allure.step("Step 5: Fill Stop 2 (Destination) details"):
        print("[Step 5/9] Filling Stop 2 (Destination) details...", flush=True)

        # Location
        create_order_page.enter_stop2_location_name(stop2["location_name"])
        create_order_page.enter_stop2_address_line1(stop2["address_line1"])
        create_order_page.enter_stop2_address_line2(stop2["address_line2"])
        create_order_page.enter_stop2_address_line3(stop2["address_line3"])
        create_order_page.enter_stop2_city(stop2["city"])
        create_order_page.enter_stop2_state(stop2["state"])
        create_order_page.enter_stop2_postal_code(stop2["postal_code"])
        create_order_page.enter_stop2_country(stop2["country"])
        create_order_page.enter_stop2_location_code(stop2["location_code"])
        create_order_page.enter_stop2_location_group(stop2["location_group"])

        # Contact
        create_order_page.enter_stop2_contact_name(stop2["contact_name"])
        create_order_page.enter_stop2_contact_phone(stop2["contact_phone"])
        create_order_page.enter_stop2_contact_email(stop2["contact_email"])
        create_order_page.enter_stop2_contact_company(stop2["contact_company"])

        # Dates & Timezone
        create_order_page.enter_stop2_requested_earliest_dropoff(stop2["requested_earliest_dropoff"])
        create_order_page.enter_stop2_requested_latest_dropoff(stop2["requested_latest_dropoff"])

        if stop2.get("timezone"):
            create_order_page.select_stop2_timezone(stop2["timezone"])

        # Toggles & Notes
        create_order_page.set_stop2_toggles(
            appointment_required=stop2.get("appointment_required"),
            save_to_address_book=stop2.get("save_to_address_book"),
            requested_date_lock=stop2.get("requested_date_lock"),
            requested_time_lock=stop2.get("requested_time_lock"),
        )
        create_order_page.enter_stop2_internal_notes(stop2["internal_notes"])
        create_order_page.enter_stop2_carrier_special_instructions(stop2["carrier_special_instructions"])
        print("  -> Stop 2 completed.", flush=True)

    # =========================================================================
    # STEP 6: FILL LINE ITEM (PRODUCT)
    # =========================================================================
    product = data["order"]["product"]
    with allure.step("Step 6: Fill Line Item (Product) details"):
        print("[Step 6/9] Filling Line Item (Product) details...", flush=True)

        create_order_page.enter_product_description(product["description"])
        create_order_page.enter_handling(product["handling"])
        create_order_page.enter_weight(product["weight"])
        create_order_page.enter_length(product["length"])
        create_order_page.enter_width(product["width"])
        create_order_page.enter_height(product["height"])
        create_order_page.enter_packaging(product["packaging"])
        create_order_page.enter_nmfc_number(product["nmfc_number"])

        if product.get("freight_class"):
            create_order_page.select_freight_class(product["freight_class"])

        if product.get("linear_feet"):
            create_order_page.enter_linear_feet(product["linear_feet"])

        create_order_page.enter_product_number(product["product_number"])
        create_order_page.enter_density(product["density"])
        create_order_page.enter_value_of_goods(product["value"])

        if product.get("sales_order_number"):
            create_order_page.enter_sales_order_number(product["sales_order_number"])

        create_order_page.set_product_toggles(
            turnable=product.get("turnable"),
            stackable=product.get("stackable"),
            hazardous=product.get("hazardous"),
            refrigerated=product.get("refrigerated"),
            save_to_product_list=product.get("save_to_product_list"),
        )
        print("  -> Line Item completed.", flush=True)

    # =========================================================================
    # STEP 7: FILL BASIC INFORMATION
    # =========================================================================
    basic_info = data["order"]["basic_information"]
    with allure.step("Step 7: Fill Basic Information"):
        print("[Step 7/9] Filling Basic Information...", flush=True)

        create_order_page.select_direction(basic_info["direction"])
        create_order_page.select_billing_terms(basic_info["billing_terms"])
        create_order_page.select_requested_mode(basic_info["requested_mode"])
        create_order_page.select_equipment_type(basic_info["equipment_type"])
        create_order_page.enter_basic_internal_notes(basic_info["internal_notes"])
        create_order_page.enter_basic_carrier_notes(basic_info["carrier_notes"])
        print("  -> Basic Information completed.", flush=True)

    # =========================================================================
    # STEP 8: SUBMIT ORDER
    # =========================================================================
    with allure.step("Step 8: Click 'Create Order' button"):
        print("[Step 8/9] Clicking 'Create Order' button...", flush=True)
        create_order_page.click_create_order()
        print("  -> Create Order clicked.", flush=True)

    # =========================================================================
    # STEP 9: VERIFY ORDER STATUS IS PENDING
    # =========================================================================
    with allure.step("Step 9: Verify order transitions to 'Pending' status"):
        print("[Step 9/9] Verifying order status is 'Pending'...", flush=True)
        create_order_page.verify_order_pending()

        # Capture and attach the final success screenshot to Allure
        create_order_page.take_screenshot("Order_Created_Pending_Status", attach_to_allure=True)

        print("\n>>> [SUCCESS] Order successfully created and verified with 'Pending' status!\n", flush=True)