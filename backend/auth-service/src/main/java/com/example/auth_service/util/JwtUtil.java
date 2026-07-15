package com.example.auth_service.util;

import com.example.auth_service.entities.User;
import io.jsonwebtoken.Claims;
import io.jsonwebtoken.Jwts;
import io.jsonwebtoken.security.Keys;
import org.springframework.beans.factory.annotation.Value;
import org.springframework.security.core.Authentication;
import org.springframework.security.core.context.SecurityContextHolder;
import org.springframework.security.core.userdetails.UsernameNotFoundException;
import org.springframework.stereotype.Component;

import javax.crypto.SecretKey;
import java.util.Date;
import java.util.Random;

@Component
public class JwtUtil {

    private final long expirationTime;
    private final SecretKey key;

    public JwtUtil(@Value("${jwt.secret}")String SECRET,
                   @Value("${jwt.expiration}")long expirationTime){
        this.key= Keys.hmacShaKeyFor(SECRET.getBytes());
        this.expirationTime=expirationTime;
    }

    public String generateToken(User user) {
        return Jwts.builder()
                .setSubject(user.getEmail())
                .claim("role", user.getRole())
                .claim("name", user.getName())
                .setIssuedAt(new Date())
                .setExpiration(new Date(System.currentTimeMillis() + expirationTime))
                .signWith(key)
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

    public boolean validateToken(User employee, String username, String token) {
        return  username.equals(employee.getEmail()) && !isTokenExpired(token);
    }

    public User getCurrentUser() {
        Authentication auth = SecurityContextHolder.getContext().getAuthentication();
        if (auth == null || !auth.isAuthenticated()) {
            throw new UsernameNotFoundException("Not authenticated");
        }
        return  (User) auth.getPrincipal();
    }

    public long getReamingExpirationTime(String token) {
        Date expiry = getUsernameFromToken(token) != null
                ? parseToken(token).getExpiration() : new Date();
        long remainingSeconds = expiry.getTime() - System.currentTimeMillis();
        return Math.max(0,remainingSeconds);

    }

    public String getOtp(){
        return  (100000 + new Random().nextInt(900000))+"";
    }
    private boolean isTokenExpired(String token) {
        return parseToken(token).getExpiration().before(new Date());
    }

}
