package io.appoena.springjava;

import java.util.concurrent.atomic.AtomicLong;

import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;
import java.net.HttpURLConnection;
import java.net.URL;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

@RestController
public class GreetingController {

	private static final String template = "Hello, %s!";
	private final AtomicLong counter = new AtomicLong();
	private static final Logger logger 
      = LoggerFactory.getLogger(GreetingController.class);

	@GetMapping("/greeting")
	public Greeting greeting(@RequestParam(value = "name", defaultValue = "World") String name) {
		try{
			logger.info("Log from Java App");
			URL url = new URL("http://python-flask:8082/api/dotnet");
			HttpURLConnection con = (HttpURLConnection) url.openConnection();
			con.setRequestMethod("GET");
			logger.info("Response: {}",con.getResponseMessage());
		}catch(Exception e){
			e.printStackTrace();
			logger.error(e.getMessage());
			logger.error(e.getStackTrace().toString());
		}
		return new Greeting(counter.incrementAndGet(), String.format(template, name));
	}

}