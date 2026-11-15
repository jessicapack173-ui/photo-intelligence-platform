MVP Issues

Implement SQLite Photo Catalog

Labels:



backend

database

mvp

Store uploaded photos in SQLite.



Requirements:



Store filename

Store filepath

Store upload timestamp

Generate photo ID

Acceptance Criteria:



Photo saved to disk

Row inserted into SQLite

Upload endpoint returns photo ID

Create Photo Metadata Schema

Labels:



architecture

database

mvp

Design metadata schema for:



Tie Dye Classification

Location Classification

Person Type Classification

Animal Classification

Schema must support future expansion.



Create Photo Listing API

Labels:



backend

database

mvp

Build GET /photos endpoint.



Requirements:



Return all photos

Return metadata

Support future filtering

Acceptance Criteria:



API returns uploaded photos

Photo metadata included

Create Tie-Dye Training Dataset

Labels:



machine-learning

mvp

Create initial tie-dye dataset structure.



Folders:



tie\_dye

not\_tie\_dye

Collect and label first training images.



Design Upload Page UI

Labels:



frontend

mvp

Create photo upload page.



Requirements:



Drag and drop upload

File selection

Upload progress

Success notification

Acceptance Criteria:



User can upload photo through UI

Backend upload endpoint called successfully

