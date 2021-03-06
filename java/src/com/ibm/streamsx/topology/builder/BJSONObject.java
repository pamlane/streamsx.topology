/*
# Licensed Materials - Property of IBM
# Copyright IBM Corp. 2015  
 */
package com.ibm.streamsx.topology.builder;

import com.ibm.json.java.JSONObject;

public abstract class BJSONObject {

    private final JSONObject json = new JSONObject();

    /**
     * Provides direct access to the JSON object, which may not be complete.
     */
    public JSONObject json() {
        return json;
    }

    public JSONObject complete() {
        return json();
    }
}
