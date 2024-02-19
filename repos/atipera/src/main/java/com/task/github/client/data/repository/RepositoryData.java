package com.task.github.client.data.repository;

import com.task.github.client.data.branch.BranchData;
import com.task.github.client.data.user.UserData;

import java.util.List;

public class RepositoryData {
    private String name;

    private UserData owner;

    private Boolean fork;

    private String branches_url;

    private List<BranchData> branchData;

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public UserData getOwner() {
        return owner;
    }

    public void setOwner(UserData owner) {
        this.owner = owner;
    }

    public Boolean getFork() {
        return fork;
    }

    public void setFork(Boolean fork) {
        this.fork = fork;
    }

    public String getBranches_url() {
        return branches_url;
    }

    public void setBranches_url(String branches_url) {
        this.branches_url = branches_url;
    }

    public List<BranchData> getBranches() {
        return branchData;
    }

    public void setBranches(List<BranchData> branchData) {
        this.branchData = branchData;
    }
}
