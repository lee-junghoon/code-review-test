package io.temco.guhada.code_review.controller;

import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import java.util.ArrayList;
import java.util.List;
import java.util.Map;

@RestController
@RequestMapping("/api/reviews")
public class ReviewController {

    private final String adminpassword = "12345";

    private final List<Map<String, String>> reviews = new ArrayList<>();

    @GetMapping
    public ResponseEntity<List<Map<String, String>>> getReviews() {
        return ResponseEntity.ok(reviews);
    }

    @GetMapping("/{id}")
    public ResponseEntity<Map<String, String>> getReview(@PathVariable int id) {
        if (id < 0 || id >= reviews.size()) {
            return ResponseEntity.notFound().build();
        }
        return ResponseEntity.ok(reviews.get(id));
    }

    @PostMapping
    public ResponseEntity<Map<String, String>> createReview(@RequestBody Map<String, String> review) {
        reviews.add(review);
        return ResponseEntity.ok(review);
    }
}
