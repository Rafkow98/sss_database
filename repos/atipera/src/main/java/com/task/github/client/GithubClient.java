package com.task.github.client;

import com.task.github.client.data.apiUrls.ApiUrls;
import com.task.github.client.data.branch.BranchData;
import com.task.github.client.data.repository.RepositoryData;
import com.task.github.client.util.UriUtil;

import org.springframework.web.client.RestClient;

import java.util.Arrays;
import java.util.List;
import java.util.Map;

public class GithubClient {
    private final RestClient restClient;

    private final ApiUrls apiUrls;

    public GithubClient(final String apiInfoUrl) {
        restClient = RestClient.create();
        apiUrls = restClient.get()
                .uri(apiInfoUrl)
                .retrieve()
                .body(ApiUrls.class);
    }

    public List<RepositoryData> getReposFromUser(String username) {
        return Arrays.asList(restClient.get()
                .uri(UriUtil.removeOptionalParametersFromUri(apiUrls.getUser_repositories_url()), Map.of("user", username))
                .retrieve()
                .body(RepositoryData[].class));
    }

    public List<BranchData> getBranchesFromRepo(RepositoryData repositoryData) {
        return Arrays.asList(restClient.get()
                .uri(UriUtil.removeOptionalParametersFromUri(repositoryData.getBranches_url()))
                .retrieve()
                .body(BranchData[].class));
    }
}
