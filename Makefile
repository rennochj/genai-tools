.PHONY: weather kill-weather 

weather:
	docker build --tag weather:latest tools/weather
	docker run -d --name mcp-server-weather -it --rm -p 8000:8000  weather:latest

kill-weather:
	docker kill mcp-server-weather