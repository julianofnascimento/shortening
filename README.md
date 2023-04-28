DJANGO URL SHORTENING APP

The route to generate a new shortened URL is "app/". If you are running this locally, it will generally be 127.0.0.1:8000/app/.

To be redirected to the corresponding shortened URL, use the empty route like this: /{short_url_key}. Locally, it will generally look like this: 127.0.0.1:8000/{short_url_key}.

To run the Docker container with the application, execute the following commands in the application's root directory:

docker build -t shortening_app .

docker run -p 8000:8000 shortening_app