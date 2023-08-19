from typing import Optional, List

from pydantic import BaseModel


class Product(BaseModel):
    id: str
    product_code: Optional[str]
    product_name: str
    variant_group: Optional[str]
    custom_menu: Optional[str]
    customisation_groups: List[str]
    attribute_codes: list
    category: str
    sub_category1: Optional[str]
    sub_category2: Optional[str]
    sub_category3: Optional[str]


class ProductAttribute(BaseModel):
    code: str
    category: str
    sub_category1: Optional[str]
    sub_category2: Optional[str]
    sub_category3: Optional[str]


class ProductAttributeValue(BaseModel):
    product: str
    category: str
    attribute_code: str
    value: str
    variant_group_id: Optional[str]


class VariantGroup(BaseModel):
    id: str
    local_id: str
    organisation: str
    attribute_codes: list


class CustomMenu(BaseModel):
    id: str
    local_id: str
    category: str
    parent_category_id: Optional[str]
    descriptor: dict
    tags: List[dict]


class CustomisationGroup(BaseModel):
    id: str
    local_id: str
    category: str
    parent_category_id: Optional[str]
    descriptor: dict
    tags: List[dict]
