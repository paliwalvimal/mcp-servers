from pydantic import BaseModel, Field, HttpUrl
from typing import Optional


class CustomDomain(BaseModel):
    id: str = Field(description="The unique identifier for the custom domain.")


class CreateShortUrlRequest(BaseModel):
    """
    Request schema for creating a new short URL.
    """

    destination: HttpUrl = Field(description="The destination or the long URL to be shortened.")
    slashtag: Optional[str] = Field(
        default=None,
        description="The slashtag or the custom identifier for the short URL.",
        min=1,
        max=40,
    )
    title: Optional[str] = Field(
        default=None,
        description="The title to identify your short URL.",
        min=3,
        max=255,
    )
    domain: Optional[CustomDomain] = Field(
        default=None, description="The unique id of the domain to use for the short URL."
    )
    description: Optional[str] = Field(
        default=None,
        description="A description/note to associate with the short link.",
        min=3,
        max=2000,
    )


class ShortUrlInfo(BaseModel):
    """
    Response schema containing the short URL and metadata.
    """

    id: str = Field(description="The unique identifier for the short URL.")
    title: str = Field(description="The title to identify your short URL.")
    destination: HttpUrl = Field(description="The destination or the long URL to be shortened.")
    shortUrl: str = Field(description="The short link pointing to the long/destination URL")


class ShortUrlInfoList(BaseModel):
    """
    Response schema containing the short URL and metadata.
    """

    urls: list[ShortUrlInfo] = Field(description="List of short URLs with details.")
