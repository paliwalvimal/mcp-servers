from pydantic import BaseModel, Field, HttpUrl, PositiveInt, field_serializer
from typing import Optional

from utils import date_parser_absolute


class ShortUrlRequest(BaseModel):
    url: HttpUrl = Field(description="The long URL that will be shortened")
    domain: Optional[str] = Field(
        default="tinyurl.com", description="The domain you would like the TinyURL to use"
    )
    alias: Optional[str] = Field(
        default=None,
        description="A short string of characters to use in the TinyURL. If ommitted, one will be randomly generated. When using a branded domain, this has a minimum length of 1 character",
        min_length=1,
        max_length=30,
    )
    tags: Optional[str] = Field(
        default=None,
        description="A comma-separated list of tags to apply to the TinyURL. Tags group and categorize TinyURLs together",
        max_length=45,
    )
    expires_at: Optional[str] = Field(
        default=None,
        description="TinyURL expiration in ISO8601 format. Set to null so TinyURL never expires. Example: 2024-10-25 10:11:12",
    )
    description: Optional[str] = Field(
        default=None,
        description="The alias description",
        min_length=3,
        max_length=1000,
    )

    @field_serializer("expires_at")
    def serialize_expires_at(self, expires_at: str):
        return date_parser_absolute(expires_at)


class ShortUrlResponse(BaseModel):
    tiny_url: Optional[str] = Field(default=None, description="The shortened URL")
    expires_at: Optional[str] = Field(
        default=None,
        description="TinyURL expiration in ISO8601 format. Example: 2024-10-25 10:11:12",
    )
    code: Optional[PositiveInt] = Field(
        default=None,
        description="Operation result code. 0 means success, anything else means failure",
    )
    errors: Optional[list[str]] = Field(default=None, description="List of errors that occurred")
