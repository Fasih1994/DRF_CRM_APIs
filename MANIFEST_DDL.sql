WHENEVER SQLERROR CONTINUE;

drop table xxyh_ims_ws_manifest_hdr;
drop table xxyh_ims_ws_manifest_lns;
drop table xxyh_jobs;

drop sequence XXYH_IMS_WS_MANIFEST_ID_S;
drop sequence XXYH_IMS_WS_MANIFEST_LINE_ID_S;

CREATE SEQUENCE XXYH_IMS_WS_MANIFEST_ID_S start with 1 nocache;
CREATE SEQUENCE XXYH_IMS_WS_MANIFEST_LINE_ID_S start with 1 nocache;

WHENEVER SQLERROR EXIT;

CREATE TABLE xxyh_ims_ws_manifest_hdr
(manifest_id                  NUMBER
,manifest_name                VARCHAR2(150)
,from_organization_id         NUMBER
,from_organization_code       VARCHAR2(3)
,to_organization_id           NUMBER
,to_organization_code         VARCHAR2(3)
,estimated_ship_date          DATE
,actual_ship_date             DATE
,airway_bill                  VARCHAR2(150)
,seal                         VARCHAR2(150)
,ship_to_name                 VARCHAR2(255)
,ship_from_name               VARCHAR2(255)
,process_status               VARCHAR2(30)
,group_name                   VARCHAR2(150)
,group_id                     NUMBER
,source_system                VARCHAR2(150)
,error_fields                 VARCHAR2(4000)
,error_code                   VARCHAR2(150)
,error_message                VARCHAR2(4000)
,user_name                    VARCHAR2(100)
,user_id                      NUMBER
,creation_date                DATE
,last_update_date             DATE
,PRIMARY KEY (manifest_id)
);


CREATE TABLE xxyh_ims_ws_manifest_lns
(manifest_line_id             NUMBER
,manifest_id                  NUMBER
,manifest_name                VARCHAR2(150)
,from_organization_code       VARCHAR2(3)
,to_organization_code         VARCHAR2(3)
,pallet                       VARCHAR2(100)
,ia_ticket_numbers            VARCHAR2(150)
,site_name                    VARCHAR2(150)
,email_date                   DATE
,inventory_item_id            NUMBER
,item_number                  VARCHAR2(40)
,item_description             VARCHAR2(255)
,quantity                     NUMBER
,shipment_header_id           NUMBER
,shipment_number              VARCHAR2(30)
,shipment_line_id             NUMBER
,requisition_number           VARCHAR2(40)
,requisition_header_id        NUMBER
,order_number                 NUMBER
,order_header_id              NUMBER
,order_line_id                NUMBER
,job_id                       NUMBER
,job_name                     VARCHAR2(240)
,jira                         VARCHAR2(150)
,gscc                         VARCHAR2(150)
,width                        NUMBER
,length                       NUMBER
,height                       NUMBER
,weight                       NUMBER
,process_status               VARCHAR2(30)
,group_name                   VARCHAR2(150)
,group_id                     NUMBER
,source_system                VARCHAR2(150)
,error_fields                 VARCHAR2(4000)
,error_code                   VARCHAR2(150)
,error_message                VARCHAR2(4000)
,user_name                    VARCHAR2(100)
,user_id                      NUMBER
,creation_date                DATE
,last_update_date             DATE
,PRIMARY KEY (manifest_line_id)
);


CREATE TABLE xxyh_jobs
(job_id             NUMBER
,job_name           VARCHAR2(100)
,PRIMARY KEY (job_id)
);


INSERT INTO xxyh_jobs VALUES (1, 'JOB1');
INSERT INTO xxyh_jobs VALUES (2, 'JOB2');
INSERT INTO xxyh_jobs VALUES (3, 'JOB3');
INSERT INTO xxyh_jobs VALUES (4, 'JOB4');
INSERT INTO xxyh_jobs VALUES (5, 'JOB5');
INSERT INTO xxyh_jobs VALUES (6, 'JOB6');
INSERT INTO xxyh_jobs VALUES (7, 'JOB7');
INSERT INTO xxyh_jobs VALUES (8, 'JOB8');
INSERT INTO xxyh_jobs VALUES (9, 'JOB9');
INSERT INTO xxyh_jobs VALUES (10, 'JOB10');

commit;

