CREATE TABLE "Category" (
  "Id" int PRIMARY KEY,
  "C_Title" varchar,
  "employe_rewards" list
);

CREATE TABLE "Staff" (
  "Id" int PRIMARY KEY,
  "Id_Category" int,
  "C_name" varchar,
  "expert" varchar,
  "exprience" varchar
);

CREATE TABLE "Project" (
  "Id" int PRIMARY KEY,
  "Id_Staff" int,
  "Id_Category" int,
  "contracting_party" varchar,
  "started" datetime,
  "deadline" datetime,
  "Work_in_progress" varchar,
  "Delay" boolean,
  "cost" float NOT NULL
);

CREATE TABLE "Pay_Slip" (
  "Id" int PRIMARY KEY,
  "Id_Staff" int,
  "salary" float NOT NULL,
  "overtime" int,
  "FinancialReward" float NOT NULL
);

COMMENT ON COLUMN "Project"."cost" IS 'It is in dollar';

COMMENT ON COLUMN "Pay_Slip"."salary" IS 'It is in dollar';

COMMENT ON COLUMN "Pay_Slip"."FinancialReward" IS 'It is in dollar';

ALTER TABLE "Staff" ADD FOREIGN KEY ("Id_Category") REFERENCES "Category" ("Id");

CREATE TABLE "Project_Staff" (
  "Project_Id_Staff" int,
  "Staff_Id" int,
  PRIMARY KEY ("Project_Id_Staff", "Staff_Id")
);

ALTER TABLE "Project_Staff" ADD FOREIGN KEY ("Project_Id_Staff") REFERENCES "Project" ("Id_Staff");

ALTER TABLE "Project_Staff" ADD FOREIGN KEY ("Staff_Id") REFERENCES "Staff" ("Id");


ALTER TABLE "Project" ADD FOREIGN KEY ("Id_Category") REFERENCES "Category" ("Id");

ALTER TABLE "Staff" ADD FOREIGN KEY ("Id") REFERENCES "Pay_Slip" ("Id_Staff");
