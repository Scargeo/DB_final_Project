# Merge Conflict Detection Demo

This document demonstrates the merge conflict detection and resolution features implemented in the Database Final Project.

## Overview

The application now includes advanced merge conflict detection to prevent data loss and handle concurrent updates safely. Here's how it works:

## Features Implemented

### 1. Version Control
- Each user record includes a `version` field that increments on every update
- Records include `last_modified` timestamp for tracking changes
- Optimistic locking prevents lost updates

### 2. Merge Properties
All API responses now include `mergeProperties` with metadata:
```json
{
  "mergeProperties": {
    "version": 1,
    "lastModified": "2025-01-01T12:00:00Z",
    "canMerge": true,
    "conflictResolution": "optimistic-locking"
  }
}
```

### 3. Conflict Detection
The system detects conflicts when:
- Two users try to update the same record simultaneously
- Version numbers don't match expected values
- Concurrent modifications occur

## API Examples

### 1. Get User with Merge Properties
```bash
GET /api/users/1
```

Response includes merge metadata:
```json
{
  "success": true,
  "data": {
    "id": 1,
    "username": "john",
    "email": "john@example.com",
    "version": 2,
    "created_at": "2025-01-01T10:00:00Z",
    "last_modified": "2025-01-01T11:30:00Z"
  },
  "mergeProperties": {
    "version": 2,
    "lastModified": "2025-01-01T11:30:00Z",
    "canMerge": true,
    "conflictResolution": "optimistic-locking"
  }
}
```

### 2. Safe Update with Version Check
```bash
PUT /api/users/1
Content-Type: application/json

{
  "username": "john_updated",
  "email": "john.new@example.com",
  "version": 2
}
```

Success response:
```json
{
  "success": true,
  "data": {
    "id": 1,
    "username": "john_updated",
    "email": "john.new@example.com",
    "version": 3,
    "last_modified": "2025-01-01T12:00:00Z"
  },
  "mergeProperties": {
    "version": 3,
    "lastModified": "2025-01-01T12:00:00Z",
    "canMerge": true,
    "conflictResolution": "resolved",
    "previousVersion": 2
  }
}
```

### 3. Conflict Detection
If someone else updated the record first:

```bash
PUT /api/users/1
Content-Type: application/json

{
  "username": "conflicting_update",
  "email": "conflict@example.com",
  "version": 2
}
```

Conflict response (HTTP 409):
```json
{
  "success": false,
  "error": "Merge conflict detected",
  "message": "Merge conflict detected. Expected version 2, but current version is 3. Please refresh and try again.",
  "conflictDetails": {
    "currentVersion": 3,
    "expectedVersion": 2,
    "currentData": {
      "id": 1,
      "username": "john_updated",
      "email": "john.new@example.com",
      "version": 3
    }
  },
  "mergeProperties": {
    "canMerge": false,
    "conflictResolution": "manual-required",
    "conflictReason": "Version mismatch"
  }
}
```

### 4. Check for Conflicts Before Update
```bash
GET /api/users/1/conflicts?username=new_name&email=new@email.com&version=2
```

Response:
```json
{
  "success": true,
  "data": {
    "hasConflict": true,
    "reason": "Version mismatch",
    "currentVersion": 3,
    "expectedVersion": 2,
    "currentData": { ... }
  }
}
```

## Conflict Resolution Workflow

1. **Get Current Data**: Always fetch the latest version before updating
2. **Include Version**: Send the version number with update requests
3. **Handle Conflicts**: If you get HTTP 409, refresh and retry
4. **Manual Resolution**: For complex conflicts, implement custom resolution logic

## Database Schema

The updated user table includes merge-related fields:

```sql
CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(255) NOT NULL UNIQUE,
    email VARCHAR(255) NOT NULL UNIQUE,
    version INT DEFAULT 1,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    last_modified TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);
```

## Benefits

✅ **Prevents Data Loss**: No more lost updates from concurrent modifications
✅ **Clear Conflict Detection**: HTTP 409 responses with detailed conflict information  
✅ **Flexible Resolution**: Multiple strategies for handling conflicts
✅ **Audit Trail**: Version tracking for change history
✅ **Production Ready**: Optimistic locking suitable for high-concurrency applications

This implementation ensures that merge conflicts cannot occur silently, protecting data integrity and providing clear feedback to applications using the API.