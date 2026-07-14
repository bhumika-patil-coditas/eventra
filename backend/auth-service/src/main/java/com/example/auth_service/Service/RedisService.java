package com.example.auth_service.Service;

import lombok.RequiredArgsConstructor;
import org.springframework.data.redis.core.RedisTemplate;
import org.springframework.stereotype.Service;

import java.util.concurrent.TimeUnit;

@Service
@RequiredArgsConstructor
public class RedisService {

    private final RedisTemplate<String, Object> redisTemplate;
    private static final String BLACKLIST_PREFIX = "blacklist:";
    private static final String OTP_PREFIX = "otp:";

    public void set(String key, Object value, long ttlMilliSeconds) {
        redisTemplate.opsForValue().set(key, value, ttlMilliSeconds, TimeUnit.MILLISECONDS);
    }

    public Object get(String key) {
        return redisTemplate.opsForValue().get(key);
    }

    public boolean exists(String key) {
        return Boolean.TRUE.equals(redisTemplate.hasKey(key));
    }

    public void delete(String key) {
        redisTemplate.delete(key);
    }

    public void blacklistToken(String token, long remainingSeconds) {
        set(BLACKLIST_PREFIX + token, "true", remainingSeconds);
    }


    public String getOtp(String email) {
        Object otp = get(OTP_PREFIX + email);
        return otp != null ? otp.toString() : null;
    }
    public void saveOtp(String email, String otp) {
        set(OTP_PREFIX + email, otp, 900000);
    }
}

