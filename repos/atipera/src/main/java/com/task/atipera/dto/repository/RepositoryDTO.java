package com.task.atipera.dto.repository;

import com.task.atipera.dto.branch.BranchDTO;

import java.util.List;

public class RepositoryDTO {
    private String name;

    private String owner;

    private List<BranchDTO> branches;

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public String getOwner() {
        return owner;
    }

    public void setOwner(String owner) {
        this.owner = owner;
    }

    public List<BranchDTO> getBranches() {
        return branches;
    }

    public void setBranches(List<BranchDTO> branches) {
        this.branches = branches;
    }
}
