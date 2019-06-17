import pytest
import asyncio
import json
from unittest.mock import (Mock)

from asynctest import CoroutineMock

from starlette.requests import Request

from ..datastore import Datastore
from .. import main

#@pytest.fixture
#def datastore_connection():
#    return CoroutineMock(Datastore, 'get_is_url_bad', return_value='{}')

HOSTNAME = "10.10.10.10:80"
PATH = "path/to/desolation"

@pytest.mark.asyncio
async def test_get_is_bad_url_true():
        expected_response_body = str({})
        expected_response_code = 204
        request_data = {"hostname_port":HOSTNAME,
                        "path_query":PATH}

        main.datastore = CoroutineMock(Datastore)
        main.datastore.get_is_url_bad.return_value= None

        request = Mock(path_params=request_data)

        response = await main.get_is_url_bad(request)

        assert response.body == expected_response_body
        assert response.status_code == expected_response_code

@pytest.mark.asyncio
async def test_get_is_bad_url_true():
        url = str(HOSTNAME + "/" + PATH)
        #TODO: This line is ridiculously long, shorten it
        expected_response_body = str({url: {url:True}}).lower().replace("\'", "\"").replace(" ", "").encode('ascii')
        expected_response_code = 200
        request_data = {"hostname_port":HOSTNAME,
                        "path_query":PATH}

        main.datastore = CoroutineMock(Datastore)
        main.datastore.get_is_url_bad.return_value={url:True}

        request = Mock(path_params=request_data)

        response = await main.get_is_url_bad(request)

        assert response.body == expected_response_body
        assert response.status_code == expected_response_code
