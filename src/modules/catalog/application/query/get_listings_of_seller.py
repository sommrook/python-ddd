from sqlalchemy.orm import Session

from modules.catalog.application import catalog_module
from modules.catalog.infrastructure.listing_repository import ListingModel
from seedwork.application.queries import Query
from seedwork.application.query_handlers import QueryResult
from seedwork.domain.value_objects import GenericUUID


class GetListingsOfSeller(Query):
    seller_id: GenericUUID


@catalog_module.query_handler
def get_listings_of_seller(query: GetListingsOfSeller, session: Session) -> QueryResult:
    # FIXME: use seller_id to filter out listings
    queryset = session.query(ListingModel)  # .filter(
    #     listing_repository.model.data['seller'].astext.cast(UUID) == query.seller_id
    # )
    result = [dict(id=row.id, **row.data) for row in queryset.all()]
    return QueryResult.success(result)
