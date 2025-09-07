from pydantic import BaseModel, Field, HttpUrl, PositiveInt
from typing import Optional


class CustomDomain(BaseModel):
    id: Optional[str] = Field(description="The unique identifier for the custom domain.")
    fullName: Optional[str] = Field(description="The fully qualified custom domain name.")


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


class ShortUrlDetails(BaseModel):
    """
    Response schema containing the short URL and metadata.
    """

    id: str = Field(description="The unique identifier for the short URL.")
    title: str = Field(description="The title to identify your short URL.")
    destination: HttpUrl = Field(description="The destination or the long URL to be shortened.")
    shortUrl: str = Field(description="The short link pointing to the long/destination URL")


class ShortUrlDetailsList(BaseModel):
    """
    Response schema containing the short URL and metadata.
    """

    urls: list[ShortUrlDetails] = Field(description="List of short URLs with details.")


class GetOrListShortUrlsRequest(BaseModel):
    """
    Request schema for getting or listing short URLs.
    """

    limit: PositiveInt = Field(
        default=25, description="The maximum number of short URLs to retrieve.", max=25
    )
    domain: Optional[CustomDomain] = Field(
        default=None, description="The unique id of the domain to use for the short URL."
    )
    slashtag: Optional[str] = Field(
        default=None,
        description="The slashtag or the custom identifier for the short URL. Custom domain is required to use this field",
    )
    dateFrom: Optional[str] = Field(
        default=None,
        description="The start date to filter short URLs by creation date. Date format must be YYYY-MM-DD",
    )
    dateTo: Optional[str] = Field(
        default=None,
        description="The end date to filter short URLs by creation date. Date format must be YYYY-MM-DD",
    )


class DeleteShortUrlRequest(BaseModel):
    """
    Request schema for deleting a short URL.
    """

    id: str = Field(description="The unique identifier of the short URL that you want to delete")
