package com.task.atipera.service;

import com.task.atipera.data.repository.Repository;

import java.util.List;

public interface RepositoryService {
    List<Repository> getReposFromUser(String username);
}
