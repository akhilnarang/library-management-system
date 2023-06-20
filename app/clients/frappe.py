import logging

import httpx

from .. import schemas


class FrappeClient:
    @staticmethod
    def get_books(request_parameters: schemas.FrappeAPIRequestParameters) -> schemas.FrappeAPIResponse:
        response = httpx.get(
            "https://frappe.io/api/method/frappe-library", params=request_parameters.dict(exclude_unset=True)
        )
        if response.status_code == 200:
            return schemas.FrappeAPIResponse.parse_obj(response.json())
        if response.headers.get("Content-Type", "") == "application/json":
            logging.error("Failed to fetch books from frappe.io", response.status_code, response.json())
        else:
            logging.error("Failed to fetch books from frappe.io", response.status_code, response.text)
        raise Exception("Failed to fetch books from frappe.io")
