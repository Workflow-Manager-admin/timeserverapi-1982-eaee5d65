from flask_smorest import Blueprint
from flask.views import MethodView
from datetime import datetime
from marshmallow import Schema, fields

blp = Blueprint(
    "Time",
    __name__,
    url_prefix="/time",
    description="Endpoint to get the current server time"
)

class TimeResponseSchema(Schema):
    current_time = fields.String(
        required=True,
        description="Current time on the server in ISO 8601 format (UTC)."
    )

# PUBLIC_INTERFACE
@blp.route("/")
class TimeResource(MethodView):
    """Endpoint to fetch the current server time in ISO 8601 format (UTC)."""

    # PUBLIC_INTERFACE
    @blp.response(200, TimeResponseSchema)
    def get(self):
        """
        Returns the current server time in ISO 8601 format (UTC).

        Returns:
            JSON object with one key 'current_time' as string
        """
        return {"current_time": datetime.utcnow().isoformat() + "Z"}
