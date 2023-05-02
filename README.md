#
This is a bundle with a simple python/flask microservice which can be run in Entando 7.1+. It satisfies the basic requirements on running on port 8081, with a context path determined by env variable SERVER_SERVLET_CONTEXT_PATH (defaults to / locally), and health check on /api/health.

## Local Development
* To run the microservice locally:
`ent bundle run python-ms`

* By default the endpoints are available at `localhost:8081/api/health` and `localhost:8081/api/random`

* On Windows you may need to set this env variable to avoid path expansion on env variables:
`export MSYS_NO_PATHCONV=1`