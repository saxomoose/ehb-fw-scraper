from scraper import serialization_service, scraper_service


def main():
    # 404616494
    enterprise_number = 502465839
    # officers_table = scraper_service.retrieve_target(enterprise_number)
    with open("./dummy/target.html", encoding="utf-8") as f:
        officers_obj = scraper_service.parse_target(f)
    officers_obj = scraper_service.parse_target(f)
    json = serialization_service.to_json(enterprise_number, officers_obj)
    print(json)
    # Send serialized json to queue


if __name__ == "__main__":
    main()
