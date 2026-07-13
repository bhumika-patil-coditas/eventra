package com.example.auth_service.util;

import com.example.auth_service.entities.User;
import com.example.auth_service.repository.UserRepository;
import io.jsonwebtoken.Claims;
import io.jsonwebtoken.Jwts;
import io.jsonwebtoken.SignatureAlgorithm;
import io.jsonwebtoken.security.Keys;
import org.springframework.beans.factory.annotation.Value;
import org.springframework.stereotype.Component;

import javax.crypto.SecretKey;
import java.util.Date;

@Component
public class JwtUtil {

    private final long expirationTime;
    private final SecretKey key;
    private final UserRepository userRepository;


    public JwtUtil(@Value("${jwt.secret}")String SECRET,
                   UserRepository userRepository,
                   @Value("${jwt.expiration}")long expirationTime){

        this.key= Keys.hmacShaKeyFor(SECRET.getBytes());
        this.userRepository = userRepository;
        this.expirationTime=expirationTime;

    }


    public String generateToken(String email) {
        User user = userRepository.findByEmail(email).orElse(null);
        assert user != null;
        return Jwts.builder()
                .setSubject(email)
                .claim("roles", user.getRole())
                .claim("username", user.getUsername())
                .setIssuedAt(new Date())
                .setExpiration(new Date(System.currentTimeMillis() + expirationTime))
                .signWith(key, SignatureAlgorithm.HS256)
                .compact();


    }

    public Claims parseToken(String token) {
        return Jwts.parser()
                .setSigningKey(key)
                .build()
                .parseClaimsJws(token)
                .getBody();
    }

    public String getUsernameFromToken(String token) {
        return parseToken(token).getSubject();
    }

    // TODO change UserDetail object with employee
    public boolean validateToken(User userDetails, String username, String token) {
        return  username.equals(userDetails.getEmail()) && !isTokenExpired(token);
    }

    private boolean isTokenExpired(String token) {
        return parseToken(token).getExpiration().before(new Date());
    }

}

