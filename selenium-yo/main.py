from booking.booking import Booking

with Booking() as bot:
    bot.go_to_first_page()
    bot.fill_in_hotel_destination_input("Bandung")
    bot.click_nth_element_of_search_results(0)
