import logging
import unittest
import time
from test_operators import DelayedTupleSourceWithLastTuple

from streamsx.topology.tester import Tester
from streamsx.topology import topology, schema

logger = logging.getLogger('streamsx.test.rest_test')

class CommonTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        """
        Initialize the logger and get the SWS username, password, and REST URL.
        :return: None
        """
        if cls is CommonTests:
            raise unittest.SkipTest("Skipping base tests.")

    def test_username_and_password(self):
        self.logger.debug("Beginning test: test_username_and_password.")
        # Ensure, at minimum, that the StreamsContext can connect and retrieve valid data from the SWS resources path
        resources = self.sc.get_resources()
        self.logger.debug("Number of retrieved resources is: " + str(len(resources)))
        self.assertGreater(len(resources), 0, msg="Returned zero resources from the \"resources\" endpoint.")

    def _verify_basic_view(self):
        q = self._view.start_data_fetch()

        try:
            view_tuple_value = q.get(block=True, timeout=25.0)
        except:
            logger.exception("Timed out while waiting for tuple.")
            raise

        self._view.stop_data_fetch()
        self.logger.debug("Returned view value in basic_view_support is " + view_tuple_value)
        self.assertTrue(view_tuple_value.startswith('hello'))

    def test_basic_view_support(self):
        self.logger.debug("Beginning test: test_basic_view_support.")
        top = topology.Topology('basicViewTest')
        # Send only one tuple
        stream = top.source(DelayedTupleSourceWithLastTuple(['hello'], 20))
        self._view = stream.view()

        # Temporary workaround for Bluemix TLS issue with views
        stream.publish(schema=schema.CommonSchema.String, topic="__test_topic::test_basic_view_support")

        self.logger.debug("Beginning compilation and submission of basic_view_support topology.")
        tester = Tester(top)
        tester.local_check = self._verify_basic_view
        tester.test(self.test_ctxtype, self.test_config)
