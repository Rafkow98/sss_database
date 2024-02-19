package com.task.github.client.data.branch;

public class BranchData {
    private String name;

    private com.task.atipera.model.commit.Commit commit;

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public com.task.atipera.model.commit.Commit getCommit() {
        return commit;
    }

    public void setCommit(com.task.atipera.model.commit.Commit commit) {
        this.commit = commit;
    }
}
