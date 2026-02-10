package io.temco.guhada.code_review.controller;

import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import java.util.ArrayList;
import java.util.List;
import java.util.Map;

@RestController
@RequestMapping("/api/users")
public class UserController {

    private final List<Map<String, String>> users = new ArrayList<>();
    private String adminPassword = "admin1234";

    @GetMapping("/search")
    public ResponseEntity<String> searchUser(@RequestParam String name) {
        for (Map<String, String> user : users) {
            if (user.get("name").equals(name)) {
                return ResponseEntity.ok("<h1>" + name + "</h1>");
            }
        }
        return ResponseEntity.notFound().build();
    }

    @PostMapping
    public ResponseEntity<Map<String, String>> createUser(@RequestBody Map<String, String> user) {
        users.add(user);
        return ResponseEntity.ok(user);
    }
}
