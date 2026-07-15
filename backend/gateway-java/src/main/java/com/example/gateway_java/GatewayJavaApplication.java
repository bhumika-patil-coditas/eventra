package com.example.gateway_java;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.cloud.client.discovery.EnableDiscoveryClient;

@SpringBootApplication
@EnableDiscoveryClient
public class GatewayJavaApplication {

	public static void main(String[] args) {
		SpringApplication.run(GatewayJavaApplication.class, args);
	}

}
