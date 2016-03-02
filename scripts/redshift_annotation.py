raw_attribute = '''public String saPropertyId;
	public String mmStateCode;
	public String mmFipsStateCode;
	public String mmFipsMuniCode;
	public String mmMuniCode;				// IGNORE_TAG, not in V3, in V2 mm_muni_code='BR',mm_fips_muni_code='011'
	public String saFipsCountyNameDfs;		// IGNORE_TAG, not in V3, replaced by MM_FIPS_COUNTY_NAME
	public String mmMuniName;
	public String saParcelNbrPrimary;
	public String saParcelNbrPrimaryFmtd;	// IGNORE_TAG, not in V3, not used anywhere
	public String saParcelNbrAlt;
	public String saOwner1;
	public String saOwner1First;
	public String saOwner1Last;
	public String saOwner1Mid;
	public String saOwner1Suf;
	public String saOwner1SpFirst;
	public String saOwner1SpMid;
	public String saOwner1SpSuf;
	public String saOwner1EtFlag;
	public String saOwner1Group;
	public String saOwner1TrustFlag;
	public String saOwner1Type;
	public String saOwner2;
	public String saOwner2First;
	public String saOwner2Last;
	public String saOwner2Mid;
	public String saOwner2Suf;
	public String saOwner2SpFirst;
	public String saOwner2SpMid;
	public String saOwner2SpSuf;
	public String saOwner2EtFlag;
	public String saOwner2Group;
	public String saOwner2TrustFlag;
	public String saOwner2Type;
	public String saOwnershipStatusCode;
	public String saCompanyFlag;
	public String saSiteHouseNbr;
	public String saSiteFraction;
	public String saSiteDir;
	public String saSiteStreetName;
	public String saSiteSuf;
	public String saSitePostDir;
	public String saSiteUnitPre;
	public String saSiteUnitVal;
	public String saSiteCityState;		// IGNORE_TAG, V3 has separate SA_SITE_CITY, SA_SITE_STATE
	public String saSiteCity;
	public String saSiteState;
	public String saSiteZip;
	public String saSiteCrrt;
	public String saSitePlus4;
	public String saMailHouseNbr;
	public String saMailFraction;
	public String saMailDir;
	public String saMailStreetName;
	public String saMailSuf;
	public String saMailPostDir;
	public String saMailUnitPre;
	public String saMailUnitVal;
	public String saMailCityState;		// IGNORE_TAG, V3 has separate SA_SITE_CITY, SA_SITE_STATE
	public String saMailCity;
	public String saMailState;
	public String saMailZip;
	public String saMailPlus4;
	public String saMailCrrt;
	public String saSiteMailSame;
	public String saLglDscrptn;
	public String saLotNbr1;
	public String saLotNbr2;
	public String saLotNbr3;
	public String saBlkNbr1;
	public String saBlkNbr2;
	public String saSubdivision;
	public String saSection;
	public String saTownship;
	public String saQuarter;
	public String saRange;
	public String saMapGridNew;			// IGNORE_TAG, not in V3, not used anywhere
	public String saMapPageNew;			// IGNORE_TAG, not in V3, not used anywhere
	public String filler;
	public String ucUseCodeMuni;		// IGNORE_TAG, not in V3, replaced by USE_CODE_MUNI
	public String ucUseCodeStd;			// IGNORE_TAG, not in V3, replaced by USE_CODE_STD
	public String saZoning;
	public String mmAssessmentYear;
	public String saExempFlag1;
	public String saExempFlag2;
	public String saExempFlag3;
	public String saExempFlag4;
	public String saExempFlag5;
	public String saExempFlag6;
	public String saExempVal1;
	public String saExempVal2;
	public String saExempVal3;
	public String saExempVal4;
	public String saExempVal5;
	public String saExempVal6;
	public String saValAssd;
	public String saValAssdImprv;
	public String saValAssdLand;
	public String saImprvPct;
	public String saValMarket;
	public String saValMarketImprv;
	public String saValMarketLand;
	public String saImprvPctMrkt;
	public String saAppraiseVal;
	public String saValAppraiseImprv;
	public String saValAppraiseLand;
	public String saImprvPctAppraise;
	public String saValFullCash;
	public String saValCurrentLimit;		// IGNORE_TAG, SA_VAL_CURRENT_LIMIT not in V3
	public String saTaxYear;
	public String saTaxVal;
	public String saTaxYearDelinq;
	public String saYrBlt;
	public String saYrBltEffect;
	public String saBldgShapeCode;
	public String saArchitectureCode;
	public String saStructureCode;
	public String saExterior1Code;
	public String saExterior2Code;			// IGNORE_TAG, SA_EXTERIOR_2_CODE not in V3
	public String saConstructionCode;
	public String saConstructionQlty;
	public String saLotDepth;
	public String saLotWidth;
	public String saLotsize;
	public String saSqftAssrTot;
	public String saSqft;
	public String saSqftDq;
	public String saFinSqft1;
	public String saFinSqft2;
	public String saFinSqft3;
	public String saFinSqft4;
	public String saFinSqftTot;
	public String saAddtnsSqft;
	public String saAtticSqft;
	public String saBsmtFinSqft;
	public String saBsmtUnfinSqft;
	public String saGrgSqft1;
	public String saGrgSqft2;				// IGNORE_TAG, SA_GRG_SQFT_2 not in V3
	public String saHeatingCooling;			// IGNORE_TAG, SA_HEATING_COOLING, not in V3
	public String saHeatingDetail;			// IGNORE_TAG, not in V3, replaced by SA_HEAT_CODE
	public String saCoolingDetail;			// IGNORE_TAG, not in V3, replaced by SA_COOL_CODE
	public String saFireplaceCode;
	public String saGarageCarport;
	public String saNbrBath;
	public String saNbrBathDq;
	public String saNbrBath1qtr;
	public String saNbrBathHalf;
	public String saNbrBath3qtr;
	public String saNbrBathFull;
	public String saNbrBedrms;
	public String saNbrRms;
	public String saNbrStories;
	public String saNbrUnits;
	public String saPoolCode;
	public String saPoolSqft;				// IGNORE_TAG, SA_POOL_SQFT not in V3
	public String saRoofCode;
	public String saViewCode;
	public String srUniqueId;
	public String maxSrDateTransfer;		// IGNORE_TAG, not in V3, not used in code anywhere
	public String saDateTransfer;
	public String saValTransfer;
	public String srBuyer;
	public String srSeller;
	public String srArmsLengthFlagDfs;
	public String srDocType;
	public String srTranType;
	public String srFullPartCode;
	public String srLndrSellerFlag;
	public String srMultApnFlagKeyed;
	public String srLoanVal1;
	public String srLoanVal2;
	public String srLoanVal3;
	public String saDocNbrFmt;
	public String srTdDocNbr1;
	public String srTdDocNbr2;
	public String srTdDocNbr3;
	public String srLndrCode1;
	public String srLndrCode2;
	public String srLndrCode3;
	public String srLndrFirstName1;
	public String srLndrLastName1;
	public String srLndrFirstName2;
	public String srLndrLastName2;
	public String srLndrFirstName3;
	public String srLndrLastName3;
	public String srLndrCreditLine1;
	public String srLndrCreditLine2;
	public String srLndrCreditLine3;
	public String srLoanType1;
	public String srLoanType2;
	public String srLoanType3;
	public String srIntRateType1;
	public String srIntRateType2;
	public String srIntRateType3;
	public String srEscrowId;
	public String srTitleCoCode;
	public String srTitleCoName;
	public String srTitleId;
	public String saDateNovalTransfer;
	public String saDocNbrNoval;
	public String saPrivacyCode;
	public String processId;
	public String sa_grg_1_code;
	public String sa_val_assd_prev;
	public String sa_bsmt_2_code;
	public String sr_unique_id_noval;
	public String sa_nbr_bath_bsmt_full;
	public String sa_yr_land_appraise;
	public String sa_inactive_parcel_flag;
	public String sa_lgl_unit;
	public String last_tax_updt;
	public String sa_patio_porch_code;
	public String sa_shell_parcel_flag;
	public String last_assr_upd;
	public String sa_bldg_code;
	public String sa_foundation_code;
	public String sa_condition_code;
	public String sa_structure_nbr;
	public String sa_heat_src_fuel_code;
	public String sa_appraise_yr;
	public String sa_nbr_bath_bsmt_half;
	public String sa_bldg_sqft;
	public String sa_tract_nbr;'''

raw_fact = '''		dqAssessor.saPropertyId=getStringValueOrEmptyOrNull(rs,"SA_PROPERTY_ID", projection);			// cannot auto generated
		dqAssessor.saHeatingDetail=getStringValueOrEmptyOrNull(rs,"SA_HEAT_CODE", projection);			// new field names in V3
		dqAssessor.saCoolingDetail=getStringValueOrEmptyOrNull(rs,"SA_COOL_CODE", projection);			// new field names in V3
		dqAssessor.mmAssessmentYear=getStringValueOrEmptyOrNull(rs,"ASSR_YEAR", projection);			// updated field name
		dqAssessor.saTaxYear=getStringValueOrEmptyOrNull(rs,"TAXYEAR", projection);						// unmatchable field name
		dqAssessor.ucUseCodeStd=getStringValueOrEmptyOrNull(rs,"USE_CODE_STD", projection);				// UC_USE_CODE_STD(v2) -> USE_CODE_STD(v3)
		dqAssessor.ucUseCodeMuni=getStringValueOrEmptyOrNull(rs,"USE_CODE_MUNI", projection);			// UC_USE_CODE_MUNI(v2) -> USE_CODE_MUNI(v3)
		dqAssessor.saFipsCountyNameDfs=getStringValueOrEmptyOrNull(rs,"MM_FIPS_COUNTY_NAME", projection);		// cannot auto generated
		dqAssessor.mmStateCode=getStringValueOrEmptyOrNull(rs,"MM_STATE_CODE", projection);
		dqAssessor.mmFipsStateCode=getStringValueOrEmptyOrNull(rs,"MM_FIPS_STATE_CODE", projection);
		dqAssessor.mmFipsMuniCode=getStringValueOrEmptyOrNull(rs,"MM_FIPS_MUNI_CODE", projection);
		dqAssessor.mmMuniName=getStringValueOrEmptyOrNull(rs,"MM_MUNI_NAME", projection);
		dqAssessor.saParcelNbrPrimary=getStringValueOrEmptyOrNull(rs,"SA_PARCEL_NBR_PRIMARY", projection);
		dqAssessor.saParcelNbrAlt=getStringValueOrEmptyOrNull(rs,"SA_PARCEL_NBR_ALT", projection);
		dqAssessor.saOwner1=getStringValueOrEmptyOrNull(rs,"SA_OWNER_1", projection);
		dqAssessor.saOwner1First=getStringValueOrEmptyOrNull(rs,"SA_OWNER_1_FIRST", projection);
		dqAssessor.saOwner1Last=getStringValueOrEmptyOrNull(rs,"SA_OWNER_1_LAST", projection);
		dqAssessor.saOwner1Mid=getStringValueOrEmptyOrNull(rs,"SA_OWNER_1_MID", projection);
		dqAssessor.saOwner1Suf=getStringValueOrEmptyOrNull(rs,"SA_OWNER_1_SUF", projection);
		dqAssessor.saOwner1SpFirst=getStringValueOrEmptyOrNull(rs,"SA_OWNER_1_SP_FIRST", projection);
		dqAssessor.saOwner1SpMid=getStringValueOrEmptyOrNull(rs,"SA_OWNER_1_SP_MID", projection);
		dqAssessor.saOwner1SpSuf=getStringValueOrEmptyOrNull(rs,"SA_OWNER_1_SP_SUF", projection);
		dqAssessor.saOwner1EtFlag=getStringValueOrEmptyOrNull(rs,"SA_OWNER_1_ET_FLAG", projection);
		dqAssessor.saOwner1Group=getStringValueOrEmptyOrNull(rs,"SA_OWNER_1_GROUP", projection);
		dqAssessor.saOwner1TrustFlag=getStringValueOrEmptyOrNull(rs,"SA_OWNER_1_TRUST_FLAG", projection);
		dqAssessor.saOwner1Type=getStringValueOrEmptyOrNull(rs,"SA_OWNER_1_TYPE", projection);
		dqAssessor.saOwner2=getStringValueOrEmptyOrNull(rs,"SA_OWNER_2", projection);
		dqAssessor.saOwner2First=getStringValueOrEmptyOrNull(rs,"SA_OWNER_2_FIRST", projection);
		dqAssessor.saOwner2Last=getStringValueOrEmptyOrNull(rs,"SA_OWNER_2_LAST", projection);
		dqAssessor.saOwner2Mid=getStringValueOrEmptyOrNull(rs,"SA_OWNER_2_MID", projection);
		dqAssessor.saOwner2Suf=getStringValueOrEmptyOrNull(rs,"SA_OWNER_2_SUF", projection);
		dqAssessor.saOwner2SpFirst=getStringValueOrEmptyOrNull(rs,"SA_OWNER_2_SP_FIRST", projection);
		dqAssessor.saOwner2SpMid=getStringValueOrEmptyOrNull(rs,"SA_OWNER_2_SP_MID", projection);
		dqAssessor.saOwner2SpSuf=getStringValueOrEmptyOrNull(rs,"SA_OWNER_2_SP_SUF", projection);
		dqAssessor.saOwner2EtFlag=getStringValueOrEmptyOrNull(rs,"SA_OWNER_2_ET_FLAG", projection);
		dqAssessor.saOwner2Group=getStringValueOrEmptyOrNull(rs,"SA_OWNER_2_GROUP", projection);
		dqAssessor.saOwner2TrustFlag=getStringValueOrEmptyOrNull(rs,"SA_OWNER_2_TRUST_FLAG", projection);
		dqAssessor.saOwner2Type=getStringValueOrEmptyOrNull(rs,"SA_OWNER_2_TYPE", projection);
		dqAssessor.saOwnershipStatusCode=getStringValueOrEmptyOrNull(rs,"SA_OWNERSHIP_STATUS_CODE", projection);
		dqAssessor.saCompanyFlag=getStringValueOrEmptyOrNull(rs,"SA_COMPANY_FLAG", projection);
		dqAssessor.saSiteHouseNbr=getStringValueOrEmptyOrNull(rs,"SA_SITE_HOUSE_NBR", projection);
		dqAssessor.saSiteFraction=getStringValueOrEmptyOrNull(rs,"SA_SITE_FRACTION", projection);
		dqAssessor.saSiteDir=getStringValueOrEmptyOrNull(rs,"SA_SITE_DIR", projection);
		dqAssessor.saSiteStreetName=getStringValueOrEmptyOrNull(rs,"SA_SITE_STREET_NAME", projection);
		dqAssessor.saSiteSuf=getStringValueOrEmptyOrNull(rs,"SA_SITE_SUF", projection);
		dqAssessor.saSitePostDir=getStringValueOrEmptyOrNull(rs,"SA_SITE_POST_DIR", projection);
		dqAssessor.saSiteUnitPre=getStringValueOrEmptyOrNull(rs,"SA_SITE_UNIT_PRE", projection);
		dqAssessor.saSiteUnitVal=getStringValueOrEmptyOrNull(rs,"SA_SITE_UNIT_VAL", projection);
		dqAssessor.saSiteCity = getStringValueOrEmptyOrNull(rs,"SA_SITE_CITY", projection);
		dqAssessor.saSiteState = getStringValueOrEmptyOrNull(rs,"SA_SITE_STATE", projection);
		dqAssessor.saSiteZip=getStringValueOrEmptyOrNull(rs,"SA_SITE_ZIP", projection);
		dqAssessor.saSiteCrrt=getStringValueOrEmptyOrNull(rs,"SA_SITE_CRRT", projection);
		dqAssessor.saSitePlus4=getStringValueOrEmptyOrNull(rs,"SA_SITE_PLUS_4", projection);
		dqAssessor.saMailHouseNbr=getStringValueOrEmptyOrNull(rs,"SA_MAIL_HOUSE_NBR", projection);
		dqAssessor.saMailFraction=getStringValueOrEmptyOrNull(rs,"SA_MAIL_FRACTION", projection);
		dqAssessor.saMailDir=getStringValueOrEmptyOrNull(rs,"SA_MAIL_DIR", projection);
		dqAssessor.saMailStreetName=getStringValueOrEmptyOrNull(rs,"SA_MAIL_STREET_NAME", projection);
		dqAssessor.saMailSuf=getStringValueOrEmptyOrNull(rs,"SA_MAIL_SUF", projection);
		dqAssessor.saMailPostDir=getStringValueOrEmptyOrNull(rs,"SA_MAIL_POST_DIR", projection);
		dqAssessor.saMailUnitPre=getStringValueOrEmptyOrNull(rs,"SA_MAIL_UNIT_PRE", projection);
		dqAssessor.saMailUnitVal=getStringValueOrEmptyOrNull(rs,"SA_MAIL_UNIT_VAL", projection);
		dqAssessor.saMailCity = getStringValueOrEmptyOrNull(rs,"SA_MAIL_CITY", projection);
		dqAssessor.saMailState=getStringValueOrEmptyOrNull(rs,"SA_MAIL_STATE", projection);
		dqAssessor.saMailZip=getStringValueOrEmptyOrNull(rs,"SA_MAIL_ZIP", projection);
		dqAssessor.saMailPlus4=getStringValueOrEmptyOrNull(rs,"SA_MAIL_PLUS_4", projection);
		dqAssessor.saMailCrrt=getStringValueOrEmptyOrNull(rs,"SA_MAIL_CRRT", projection);
		dqAssessor.saSiteMailSame=getStringValueOrEmptyOrNull(rs,"SA_SITE_MAIL_SAME", projection);
		dqAssessor.saLglDscrptn=getStringValueOrEmptyOrNull(rs,"SA_LGL_DSCRPTN", projection);
		dqAssessor.saLotNbr1=getStringValueOrEmptyOrNull(rs,"SA_LOT_NBR_1", projection);
		dqAssessor.saLotNbr2=getStringValueOrEmptyOrNull(rs,"SA_LOT_NBR_2", projection);
		dqAssessor.saLotNbr3=getStringValueOrEmptyOrNull(rs,"SA_LOT_NBR_3", projection);
		dqAssessor.saBlkNbr1=getStringValueOrEmptyOrNull(rs,"SA_BLK_NBR_1", projection);
		dqAssessor.saBlkNbr2=getStringValueOrEmptyOrNull(rs,"SA_BLK_NBR_2", projection);
		dqAssessor.saSubdivision=getStringValueOrEmptyOrNull(rs,"SA_SUBDIVISION", projection);
		dqAssessor.saSection=getStringValueOrEmptyOrNull(rs,"SA_SECTION", projection);
		dqAssessor.saTownship=getStringValueOrEmptyOrNull(rs,"SA_TOWNSHIP", projection);
		dqAssessor.saQuarter=getStringValueOrEmptyOrNull(rs,"SA_QUARTER", projection);
		dqAssessor.saRange=getStringValueOrEmptyOrNull(rs,"SA_RANGE", projection);
		dqAssessor.filler=getStringValueOrEmptyOrNull(rs,"FILLER", projection);
		dqAssessor.saZoning=getStringValueOrEmptyOrNull(rs,"SA_ZONING", projection);
		dqAssessor.saExempFlag1=getStringValueOrEmptyOrNull(rs,"SA_EXEMP_FLAG_1", projection);
		dqAssessor.saExempFlag2=getStringValueOrEmptyOrNull(rs,"SA_EXEMP_FLAG_2", projection);
		dqAssessor.saExempFlag3=getStringValueOrEmptyOrNull(rs,"SA_EXEMP_FLAG_3", projection);
		dqAssessor.saExempFlag4=getStringValueOrEmptyOrNull(rs,"SA_EXEMP_FLAG_4", projection);
		dqAssessor.saExempFlag5=getStringValueOrEmptyOrNull(rs,"SA_EXEMP_FLAG_5", projection);
		dqAssessor.saExempFlag6=getStringValueOrEmptyOrNull(rs,"SA_EXEMP_FLAG_6", projection);
		dqAssessor.saExempVal1=getStringValueOrEmptyOrNull(rs,"SA_EXEMP_VAL_1", projection);
		dqAssessor.saExempVal2=getStringValueOrEmptyOrNull(rs,"SA_EXEMP_VAL_2", projection);
		dqAssessor.saExempVal3=getStringValueOrEmptyOrNull(rs,"SA_EXEMP_VAL_3", projection);
		dqAssessor.saExempVal4=getStringValueOrEmptyOrNull(rs,"SA_EXEMP_VAL_4", projection);
		dqAssessor.saExempVal5=getStringValueOrEmptyOrNull(rs,"SA_EXEMP_VAL_5", projection);
		dqAssessor.saExempVal6=getStringValueOrEmptyOrNull(rs,"SA_EXEMP_VAL_6", projection);
		dqAssessor.saValAssd=getStringValueOrEmptyOrNull(rs,"SA_VAL_ASSD", projection);
		dqAssessor.saValAssdImprv=getStringValueOrEmptyOrNull(rs,"SA_VAL_ASSD_IMPRV", projection);
		dqAssessor.saValAssdLand=getStringValueOrEmptyOrNull(rs,"SA_VAL_ASSD_LAND", projection);
		dqAssessor.saImprvPct=getStringValueOrEmptyOrNull(rs,"SA_IMPRV_PCT", projection);
		dqAssessor.saValMarket=getStringValueOrEmptyOrNull(rs,"SA_VAL_MARKET", projection);
		dqAssessor.saValMarketImprv=getStringValueOrEmptyOrNull(rs,"SA_VAL_MARKET_IMPRV", projection);
		dqAssessor.saValMarketLand=getStringValueOrEmptyOrNull(rs,"SA_VAL_MARKET_LAND", projection);
		dqAssessor.saImprvPctMrkt=getStringValueOrEmptyOrNull(rs,"SA_IMPRV_PCT_MRKT", projection);
		dqAssessor.saAppraiseVal=getStringValueOrEmptyOrNull(rs,"SA_APPRAISE_VAL", projection);
		dqAssessor.saValAppraiseImprv=getStringValueOrEmptyOrNull(rs,"SA_VAL_APPRAISE_IMPRV", projection);
		dqAssessor.saValAppraiseLand=getStringValueOrEmptyOrNull(rs,"SA_VAL_APPRAISE_LAND", projection);
		dqAssessor.saImprvPctAppraise=getStringValueOrEmptyOrNull(rs,"SA_IMPRV_PCT_APPRAISE", projection);
		dqAssessor.saValFullCash=getStringValueOrEmptyOrNull(rs,"SA_VAL_FULL_CASH", projection);
		dqAssessor.saTaxVal=getStringValueOrEmptyOrNull(rs,"SA_TAX_VAL", projection);
		dqAssessor.saTaxYearDelinq=getStringValueOrEmptyOrNull(rs,"SA_TAX_YEAR_DELINQ", projection);
		dqAssessor.saYrBlt=getStringValueOrEmptyOrNull(rs,"SA_YR_BLT", projection);
		dqAssessor.saYrBltEffect=getStringValueOrEmptyOrNull(rs,"SA_YR_BLT_EFFECT", projection);
		dqAssessor.saBldgShapeCode=getStringValueOrEmptyOrNull(rs,"SA_BLDG_SHAPE_CODE", projection);
		dqAssessor.saArchitectureCode=getStringValueOrEmptyOrNull(rs,"SA_ARCHITECTURE_CODE", projection);
		dqAssessor.saStructureCode=getStringValueOrEmptyOrNull(rs,"SA_STRUCTURE_CODE", projection);
		dqAssessor.saExterior1Code=getStringValueOrEmptyOrNull(rs,"SA_EXTERIOR_1_CODE", projection);
		dqAssessor.saConstructionCode=getStringValueOrEmptyOrNull(rs,"SA_CONSTRUCTION_CODE", projection);
		dqAssessor.saConstructionQlty=getStringValueOrEmptyOrNull(rs,"SA_CONSTRUCTION_QLTY", projection);
		dqAssessor.saLotDepth=getStringValueOrEmptyOrNull(rs,"SA_LOT_DEPTH", projection);
		dqAssessor.saLotWidth=getStringValueOrEmptyOrNull(rs,"SA_LOT_WIDTH", projection);
		dqAssessor.saLotsize=getStringValueOrEmptyOrNull(rs,"SA_LOTSIZE", projection);
		dqAssessor.saSqftAssrTot=getStringValueOrEmptyOrNull(rs,"SA_SQFT_ASSR_TOT", projection);
		dqAssessor.saSqft=getStringValueOrEmptyOrNull(rs,"SA_SQFT", projection);
		dqAssessor.saSqftDq=getStringValueOrEmptyOrNull(rs,"SA_SQFT_DQ", projection);
		dqAssessor.saFinSqft1=getStringValueOrEmptyOrNull(rs,"SA_FIN_SQFT_1", projection);
		dqAssessor.saFinSqft2=getStringValueOrEmptyOrNull(rs,"SA_FIN_SQFT_2", projection);
		dqAssessor.saFinSqft3=getStringValueOrEmptyOrNull(rs,"SA_FIN_SQFT_3", projection);
		dqAssessor.saFinSqft4=getStringValueOrEmptyOrNull(rs,"SA_FIN_SQFT_4", projection);
		dqAssessor.saFinSqftTot=getStringValueOrEmptyOrNull(rs,"SA_FIN_SQFT_TOT", projection);
		dqAssessor.saAddtnsSqft=getStringValueOrEmptyOrNull(rs,"SA_ADDTNS_SQFT", projection);
		dqAssessor.saAtticSqft=getStringValueOrEmptyOrNull(rs,"SA_ATTIC_SQFT", projection);
		dqAssessor.saBsmtFinSqft=getStringValueOrEmptyOrNull(rs,"SA_BSMT_FIN_SQFT", projection);
		dqAssessor.saBsmtUnfinSqft=getStringValueOrEmptyOrNull(rs,"SA_BSMT_UNFIN_SQFT", projection);
		dqAssessor.saGrgSqft1=getStringValueOrEmptyOrNull(rs,"SA_GRG_SQFT_1", projection);
		dqAssessor.saFireplaceCode=getStringValueOrEmptyOrNull(rs,"SA_FIREPLACE_CODE", projection);
		dqAssessor.saGarageCarport=getStringValueOrEmptyOrNull(rs,"SA_GARAGE_CARPORT", projection);
		dqAssessor.saNbrBath=getStringValueOrEmptyOrNull(rs,"SA_NBR_BATH", projection);
		dqAssessor.saNbrBathDq=getStringValueOrEmptyOrNull(rs,"SA_NBR_BATH_DQ", projection);
		dqAssessor.saNbrBath1qtr=getStringValueOrEmptyOrNull(rs,"SA_NBR_BATH_1QTR", projection);
		dqAssessor.saNbrBathHalf=getStringValueOrEmptyOrNull(rs,"SA_NBR_BATH_HALF", projection);
		dqAssessor.saNbrBath3qtr=getStringValueOrEmptyOrNull(rs,"SA_NBR_BATH_3QTR", projection);
		dqAssessor.saNbrBathFull=getStringValueOrEmptyOrNull(rs,"SA_NBR_BATH_FULL", projection);
		dqAssessor.saNbrBedrms=getStringValueOrEmptyOrNull(rs,"SA_NBR_BEDRMS", projection);
		dqAssessor.saNbrRms=getStringValueOrEmptyOrNull(rs,"SA_NBR_RMS", projection);
		dqAssessor.saNbrStories=getStringValueOrEmptyOrNull(rs,"SA_NBR_STORIES", projection);
		dqAssessor.saNbrUnits=getStringValueOrEmptyOrNull(rs,"SA_NBR_UNITS", projection);
		dqAssessor.saPoolCode=getStringValueOrEmptyOrNull(rs,"SA_POOL_CODE", projection);
		dqAssessor.saRoofCode=getStringValueOrEmptyOrNull(rs,"SA_ROOF_CODE", projection);
		dqAssessor.saViewCode=getStringValueOrEmptyOrNull(rs,"SA_VIEW_CODE", projection);
		dqAssessor.srUniqueId=getStringValueOrEmptyOrNull(rs,"SR_UNIQUE_ID", projection);
		dqAssessor.saDateTransfer=getStringValueOrEmptyOrNull(rs,"SA_DATE_TRANSFER", projection);
		dqAssessor.saValTransfer=getStringValueOrEmptyOrNull(rs,"SA_VAL_TRANSFER", projection);
		dqAssessor.saDocNbrFmt=getStringValueOrEmptyOrNull(rs,"SA_DOC_NBR_FMT", projection);
		dqAssessor.saDateNovalTransfer=getStringValueOrEmptyOrNull(rs,"SA_DATE_NOVAL_TRANSFER", projection);
		dqAssessor.saDocNbrNoval=getStringValueOrEmptyOrNull(rs,"SA_DOC_NBR_NOVAL", projection);
		dqAssessor.saPrivacyCode=getStringValueOrEmptyOrNull(rs,"SA_PRIVACY_CODE", projection);
		dqAssessor.processId=getStringValueOrEmptyOrNull(rs,"PROCESS_ID", projection);
		dqAssessor.sa_grg_1_code=getStringValueOrEmptyOrNull(rs,"SA_GRG_1_CODE",projection);
		dqAssessor.sa_val_assd_prev=getStringValueOrEmptyOrNull(rs,"SA_VAL_ASSD_PREV",projection);
		dqAssessor.sa_bsmt_2_code=getStringValueOrEmptyOrNull(rs,"SA_BSMT_2_CODE",projection);
		dqAssessor.sr_unique_id_noval=getStringValueOrEmptyOrNull(rs,"SR_UNIQUE_ID_NOVAL",projection);
		dqAssessor.sa_nbr_bath_bsmt_full=getStringValueOrEmptyOrNull(rs,"SA_NBR_BATH_BSMT_FULL",projection);
		dqAssessor.sa_yr_land_appraise=getStringValueOrEmptyOrNull(rs,"SA_YR_LAND_APPRAISE",projection);
		dqAssessor.sa_inactive_parcel_flag=getStringValueOrEmptyOrNull(rs,"SA_INACTIVE_PARCEL_FLAG",projection);
		dqAssessor.sa_lgl_unit=getStringValueOrEmptyOrNull(rs,"SA_LGL_UNIT",projection);
		dqAssessor.last_tax_updt=getStringValueOrEmptyOrNull(rs,"LAST_TAX_UPDT",projection);
		dqAssessor.sa_patio_porch_code=getStringValueOrEmptyOrNull(rs,"SA_PATIO_PORCH_CODE",projection);
		dqAssessor.sa_shell_parcel_flag=getStringValueOrEmptyOrNull(rs,"SA_SHELL_PARCEL_FLAG",projection);
		dqAssessor.last_assr_upd=getStringValueOrEmptyOrNull(rs,"LAST_ASSR_UPD",projection);
		dqAssessor.sa_bldg_code=getStringValueOrEmptyOrNull(rs,"SA_BLDG_CODE",projection);
		dqAssessor.sa_foundation_code=getStringValueOrEmptyOrNull(rs,"SA_FOUNDATION_CODE",projection);
		dqAssessor.sa_condition_code=getStringValueOrEmptyOrNull(rs,"SA_CONDITION_CODE",projection);
		dqAssessor.sa_structure_nbr=getStringValueOrEmptyOrNull(rs,"SA_STRUCTURE_NBR",projection);
		dqAssessor.sa_heat_src_fuel_code=getStringValueOrEmptyOrNull(rs,"SA_HEAT_SRC_FUEL_CODE",projection);
		dqAssessor.sa_appraise_yr=getStringValueOrEmptyOrNull(rs,"SA_APPRAISE_YR",projection);
		dqAssessor.sa_nbr_bath_bsmt_half=getStringValueOrEmptyOrNull(rs,"SA_NBR_BATH_BSMT_HALF",projection);
		dqAssessor.sa_bldg_sqft=getStringValueOrEmptyOrNull(rs,"SA_BLDG_SQFT",projection);
		dqAssessor.sa_tract_nbr=getStringValueOrEmptyOrNull(rs,"SA_TRACT_NBR",projection);'''
amenity_raw = '''MM_FIPS_STATE_CODE SMALLINT not null, /*Federal Information Processing Standards (FIPS) code for the state.  */
MM_FIPS_MUNI_CODE SMALLINT not null, /*Federal Information Processing Standards (FIPS) code for the county.  */
MM_FIPS_COUNTY_NAME VARCHAR(35) not null, /*The county name associated with the Federal Information Processing Standards (FIPS) county code.  */
SA_OWNER_1 VARCHAR(50), /*The full unparsed primary owner's name.  The primary owner is the individual or entity who holds the most interest in a property. Married couples are considered one entity.*/
SA_OWNER_1_FIRST VARCHAR(50), /*The first name of the primary owner of the property*/
SA_OWNER_1_MID VARCHAR(20), /*The middle name of the primary owner of a property*/
SA_OWNER_1_LAST VARCHAR(50), /*The primary owner's last name.  If the primary owner is a company the company name will be present in this field and SA_OWNER_1_FIRST will be blank.*/
SA_OWNER_1_SUF VARCHAR(5), /*The suffix associated with the primary owner of the property (Jr. III, etc).*/
SA_OWNER_1_SP_FIRST VARCHAR(20), /*The first name of the primary property owner's spouse*/
SA_OWNER_1_SP_MID VARCHAR(20), /*The middle name of the primary property owner's spouse*/
SA_OWNER_1_SP_SUF VARCHAR(5), /*The suffix of the primary property owner's spouse (Jr. III, etc).*/
SA_OWNER_1_GROUP VARCHAR(15), /*Name of other primary group members or individual primary property owners. This group or individual will not be the spouse of the primary owner*/
SA_OWNER_1_ET_FLAG VARCHAR(1), /*Identifies that there are more than 3 owners contained within the primary owner field (ETAL) or that the primary owner has a spouse (ETUX), or both.*/
SA_OWNER_1_TRUST_FLAG VARCHAR(1), /*Flag that indicates if the primary property owner is a trust.*/
SA_OWNER_1_TYPE VARCHAR(1), /*Indicates if the primary owner is an individual, a company or deceased.*/
SA_OWNER_2 VARCHAR(50), /*The full unparsed name of secondary property owner.*/
SA_OWNER_2_FIRST VARCHAR(50), /*The first name of the secondary owner of the property*/
SA_OWNER_2_MID VARCHAR(20), /*The middle name of the secondary owner of the property*/
SA_OWNER_2_LAST VARCHAR(20), /*The secondary owner's last name.  If the secondary owner is a company the company name will be present in this field and SA_OWNER_2_FIRST will be blank.*/
SA_OWNER_2_SUF VARCHAR(5), /*The suffix associated with the secondary owner of the property (Jr. III, etc).*/
SA_OWNER_2_SP_FIRST VARCHAR(20), /*The first name of the secondary owner's spouse.*/
SA_OWNER_2_SP_MID VARCHAR(20), /* The middle name of the secondary owner's spouse.*/
SA_OWNER_2_SP_SUF VARCHAR(5), /*The suffix of the secondary property owner's spouse (Jr. III, etc).*/
SA_OWNER_2_GROUP VARCHAR(15), /*Name of other secondary group members or individual secondary property owners. This group or individual will not be the spouse of the secondary owner*/
SA_OWNER_2_ET_FLAG VARCHAR(1), /*Identifies that there are more than 3 owners contained within the secondary owner field (ETAL) or that the secondary owner has a spouse (ETUX), or both.*/
SA_OWNER_2_TRUST_FLAG VARCHAR(1), /*Flag that indicates if the secondary property owner is a trust.*/
SA_OWNER_2_TYPE VARCHAR(1), /*Indicates if the secondary owner is an individual, a company or deceased.*/
SA_OWNERSHIP_STATUS_CODE VARCHAR(2), /*Indicates the ownership vesting type. Generally a relationship between owners or type of entity.*/
SA_COMPANY_FLAG VARCHAR(1), /*Indicates if the property is owned by a non-individual entity.  */
SA_SITE_HOUSE_NBR VARCHAR(20), /*The Site Address House Number*/
SA_SITE_FRACTION VARCHAR(10), /*The Site Address house number fraction (1/2, etc).*/
SA_SITE_DIR VARCHAR(2), /*The pre directional  of the site address.*/
SA_SITE_STREET_NAME VARCHAR(40), /*The Site Address Street Name.*/
SA_SITE_SUF VARCHAR(4), /*The Site Address Street Name Suffix.*/
SA_SITE_POST_DIR VARCHAR(2), /*The post-directional of the site address.*/
SA_SITE_UNIT_PRE VARCHAR(10), /*The Site Address Unit Number Prefix.*/
SA_SITE_UNIT_VAL VARCHAR(6), /*The Site Address Unit Number.*/
SA_SITE_CITY VARCHAR(30), /*The Site Address City Name*/
SA_SITE_STATE VARCHAR(2), /*The Site State Code*/
SA_SITE_ZIP INT, /*The Site Address Zip Code.*/
SA_SITE_PLUS_4 SMALLINT, /*TheSite Address Zip  plus 4 Code.*/
SA_SITE_CRRT VARCHAR(4), /*Site Address Postal Carrier Route. A Carrier Route includes city routes, rural routes, highway contract routes, Post Office_ box sections and general delivery units.*/
SA_MAIL_HOUSE_NBR VARCHAR(20), /*The Mailing Address House Number*/
SA_MAIL_FRACTION VARCHAR(10), /*The Mailing Address house number fraction (1/2, etc).*/
SA_MAIL_DIR VARCHAR(2), /*The pre-directional of the mailing address. */
SA_MAIL_STREET_NAME VARCHAR(50), /*The Mailing Address Street Name. */
SA_MAIL_SUF VARCHAR(4), /*The Mailing Address Street Name Suffix.*/
SA_MAIL_POST_DIR VARCHAR(2), /*The post-directional of the mailing address.*/
SA_MAIL_UNIT_PRE VARCHAR(10), /*The Mailing Address Unit Number Prefix.*/
SA_MAIL_UNIT_VAL VARCHAR(6), /*The Mailing Address Unit Number.*/
SA_MAIL_CITY VARCHAR(50), /*The Mailing Address City Name*/
SA_MAIL_STATE VARCHAR(2), /*The Mailing Address State Name.*/
SA_MAIL_ZIP INT, /*The Mailing Address Zip Code.*/
SA_MAIL_PLUS_4 SMALLINT, /*The Mailing Address Zip plus 4 Code.*/
SA_MAIL_CRRT VARCHAR(4), /*The Mailing Address Postal Carrier Route. A Carrier Route includes city routes, rural routes, highway contract routes, Post Office_ box sections and general delivery units.*/
SA_SITE_MAIL_SAME VARCHAR(1), /*Indicates if the site and mail address are the same, Owner Occupied.  */
SA_LGL_DSCRPTN VARCHAR(255), /*A legally acceptable description of real property that is sufficient to locate and identify a property.  Not a metes and bounds description.*/
SA_LOT_NBR_1 VARCHAR(6), /*The primary or first lot number from the legal description for the property. Usually refers to a portion of the subdivision.*/
SA_LOT_NBR_2 VARCHAR(6), /*Additional lot, considered secondary lot.*/
SA_LOT_NBR_3 VARCHAR(6), /* Additional lot, considered third lot.*/
SA_BLK_NBR_1 VARCHAR(5), /*The first block number present in the legal description*/
SA_BLK_NBR_2 VARCHAR(5), /*The second block numberr present in the legal description*/
SA_SUBDIVISION VARCHAR(30), /* Indicates the subdivision in which the property lies*/
SA_TRACT_NBR INT, /*The tract number as present in the legal description*/
SA_LGL_UNIT VARCHAR(10), /*The legal unit number present in the legal description*/
USE_CODE_STD VARCHAR(4), /*The DataQuick property use type code mapped to the jurisdictional use code.*/
USE_CODE_MUNI VARCHAR(6), /*The jurisdiction-specfic property use type indicator.  */
SA_ZONING VARCHAR(13), /*Thezoning codeassigned to a property by a county/city/other government bureau which defines the allowed size, type, structure, nature, and use of property and/or buildings.This code is not standardized and is subjective to the specific local government regulation.*/
ASSR_YEAR VARCHAR(4), /*The year of the assessment provided by the jurisdictional Assessor Office.  Assessments are not necessarily run every year, and sometimes assessments are for the year prior and sometimes assessments are for the year following.*/
SA_VAL_ASSD INT, /*A tax assessor's determination of the value of the property in order to calculate the tax amount owed.*/
SA_VAL_ASSD_LAND INT, /*The value of the land that is taxed by the assessor.*/
SA_VAL_ASSD_IMPRV INT, /* The value of the improvements that are taxed by the assessor.*/
SA_IMPRV_PCT DECIMAL, /*The percent of total assessed value represented by improvements. */
SA_APPRAISE_YR SMALLINT, /*Year for the corresponding SA_APPRAISE_VAL.*/
SA_YR_LAND_APPRAISE SMALLINT, /*Year in which the last land appraisal occurred*/
SA_APPRAISE_VAL INT, /*Assessor provided appraisal value, used in determining property tax values*/
SA_VAL_APPRAISE_LAND INT, /*The assessor's appraised value of the land.*/
SA_VAL_APPRAISE_IMPRV INT, /*The assessor's appraised value of the improvement(s).*/
SA_IMPRV_PCT_APPRAISE DECIMAL, /*The percent of total appraisal value represented by improvements.  */
SA_VAL_MARKET INT, /*Market value as determined by assessor.*/
SA_VAL_MARKET_LAND INT, /*Market value of land as determined by assessor.*/
SA_VAL_MARKET_IMPRV INT, /*Market value of improvements as determined by assessor.*/
SA_IMPRV_PCT_MRKT DECIMAL, /*The percent of total market value represented by improvements.  */
SA_VAL_FULL_CASH INT, /*The amount of cash or its equivalent that the property would bring if exposed for sale in the open market.*/
SA_VAL_ASSD_PREV INT, /*Previous assessed value of the property.*/
TAXYEAR VARCHAR(4), /*The year for which the property taxes are paid.*/
SA_TAX_VAL DECIMAL, /*Indicates the property tax amount billed to the owner of the property*/
SA_TAX_YEAR_DELINQ SMALLINT, /*Indicates the most recent year of tax deliquency.  Not the latest year that a deliquency existed, but rather the last year for which taxes are delinquent.*/
LAST_ASSR_UPD DATE, /*The date that the last full Assessor update file was received from the jurisdictional Assessor's Office.*/
LAST_TAX_UPDT DATE, /*The date that the last tax update file was received from the jurisdictional Assessor's office.*/
SA_ADDTNS_SQFT SMALLINT, /*The identified addition's square feet.*/
SA_ARCHITECTURE_CODE VARCHAR(1), /*Indicates the architectural style of the structure.*/
SA_ATTIC_SQFT SMALLINT, /*Total area, in square feet, of the attic present on the property*/
SA_BLDG_CODE VARCHAR(2), /*This field contains a 2 character code that indicates the structure type of the property*/
SA_BLDG_SHAPE_CODE VARCHAR(2), /*Code indicating the shape of the building. */
SA_BLDG_SQFT SMALLINT, /*The square footage of the building/structure on the property.*/
SA_BSMT_2_CODE VARCHAR(2), /*Code indicating the state, use or type of the basement on the property*/
SA_BSMT_FIN_SQFT SMALLINT, /*The square footage of the finished portion of the basement on the property.*/
SA_BSMT_UNFIN_SQFT SMALLINT, /*The square footage of the unfinished portion of the basement on the property.*/
SA_CONDITION_CODE DECIMAL, /*Code indicating the state/condition of a particular property*/
SA_CONSTRUCTION_CODE VARCHAR(2), /*Indicates the material used in the construction of the framework for the structure on the  property.*/
SA_CONSTRUCTION_QLTY DECIMAL, /*An appraiser rating indicating the quality of construction of the structure on the property. */
SA_COOL_CODE VARCHAR(2), /*Code indicating the presence/absence of a cooling mechanism in a particular property. It, alternatively, can also indicate the type of the available cooling mechanism*/
SA_EXTERIOR_1_CODE VARCHAR(2), /*Code indicating the primary material used as an exterior sheathing/cover for the structure on the property*/
SA_FIN_SQFT_1 INT, /*The sum total of the area covered by ground floors of all the buildings on the property.*/
SA_FIN_SQFT_2 INT, /*The sum total of the area covered by second floors of all the buildings on the property.*/
SA_FIN_SQFT_3 INT, /*The sum total of the area covered by third floors of all the buildings on the property.*/
SA_FIN_SQFT_4 INT, /*The sum total of the area covered by fourth floors of all the buildings on the property.*/
SA_FIN_SQFT_TOT INT, /*Total finished area of all the buildings on the property*/
SA_FIREPLACE_CODE VARCHAR(2), /*Contains a 2 character code that indicates the presence/absence of a fireplace. It also indicates the type of fireplace the property contains.*/
SA_FOUNDATION_CODE VARCHAR(2), /*Indicates the type of foundantion for the primary structure on the property*/
SA_GARAGE_CARPORT VARCHAR(3), /*Indicates the presence of a garage or carport, if it is attached or detached and the number of spaces.  */
SA_GRG_1_CODE VARCHAR(2), /*Indicates the type of the primary garage.  */
SA_GRG_SQFT_1 SMALLINT, /*Indicates the total square footage of the primary garage on the property.*/
SA_HEAT_CODE VARCHAR(2), /*Indicates the primary heating system or method on a property*/
SA_HEAT_SRC_FUEL_CODE VARCHAR(2), /*Indicates the primary heating fuel used.  */
SA_LOT_DEPTH SMALLINT, /*Indicates the depth of the lot, in feet.*/
SA_LOT_WIDTH SMALLINT, /*The number of feet at the front of the property.  */
SA_LOTSIZE DECIMAL, /*The lot size expressed in square feet.  */
SA_NBR_BATH DECIMAL, /*Indicates the total number of baths for all structures on a property. This field is calculated using the number of occurs of discrete bathrooms on a property. For example, a property containing a one quarter bath, half bath and full bath would have an SA_NBR_BATH value of three.*/
SA_NBR_BATH_1QTR SMALLINT, /*Indicates the number of one-quarter baths for all structures on a property. A one-quarter bath is defined as having a toilet only*/
SA_NBR_BATH_HALF SMALLINT, /*Indicates the number of half baths for all structures on a property. A half bath is defined as having a sink and a toilet only*/
SA_NBR_BATH_3QTR SMALLINT, /*Indicates the number of three quarter baths for all structures on a property. A three-quarters bath is defined as having a toilet, a sink and a shower.*/
SA_NBR_BATH_FULL SMALLINT, /*Indicates the number of full baths for all structures on a property. A full bath is defined as havingt a toilet, a sink, and a bathtub.*/
SA_NBR_BATH_BSMT_HALF SMALLINT, /*Indicates the number of half-baths in the basement for all structures on a property. A half-bath is defined as having a toilet and a sink.*/
SA_NBR_BATH_BSMT_FULL SMALLINT, /*Indicates the number of full baths in the basement for all structures on a property. A full bath is defined as having a toilet, a sink, and a bathtub.*/
SA_NBR_BATH_DQ DECIMAL, /*Indicates the number of baths in real estate terms. For example, a property containing a one quarter bath, half bath and full bath would have an SA_NBR_BATH value of 1.75.  */
SA_NBR_BEDRMS SMALLINT, /*Indicates the number of bedrooms for all structures on the property.*/
SA_NBR_RMS SMALLINT, /*Indicates the total number of rooms for all structures on the property*/
SA_NBR_STORIES SMALLINT, /*Indicates the total number of stories for all structures on the property*/
SA_NBR_UNITS SMALLINT, /*Indicates the total number of units for all structures on the property. This field will include the number of apartment or commercial units.*/
SA_PATIO_PORCH_CODE VARCHAR(2), /*Indicates the presence or type of patio or porch.  */
SA_POOL_CODE VARCHAR(2), /*Indicates if there is a pool on the property and/or pool construction material.*/
SA_PRIVACY_CODE VARCHAR(1), /*Indicates the Do Not Call/Do Not Mail status of the property owner.*/
SA_ROOF_CODE VARCHAR(2), /*Indicates the finished material of which the roof is made*/
SA_SQFT INT, /*The total square footage of the living area of all structures on the property*/
SA_SQFT_ASSR_TOT INT, /*The total Assessor raw square footage of all buildings on the property*/
SA_SQFT_DQ INT, /*Codified field to signify at the record level which type of square footage is represented in the SA_SQFT field.*/
SA_STRUCTURE_CODE VARCHAR(2), /*Indicates the structural style or the presence of specific style elements in the structure.*/
SA_STRUCTURE_NBR SMALLINT, /*Indicates number of structures on the property*/
SA_VIEW_CODE VARCHAR(2), /*Indicates the presence and type of view from the property. */
SA_YR_BLT SMALLINT, /*Year in which the primary structure was built on the property*/
SA_YR_BLT_EFFECT SMALLINT, /*Year in which ""permitted"" major improvements were made to the property*/
SR_UNIQUE_ID INT, /*The DataQuick internal unique transaction identifier.  In the Assessor data this liks to the last resale transaction*/
SR_UNIQUE_ID_NOVAL INT, /*The DataQuick internal unique transaction identifier.  In the Assessor data this liks to the last noval transaction*/
SA_DATE_TRANSFER INT, /*Document date for the most recent arms-length ownership transfer*/
SA_VAL_TRANSFER INT, /*Sale amount for the most recent ownership transfer.*/
SA_DOC_NBR_FMT VARCHAR(20), /*Document number for the most recent arms-length ownership transfer as provided by the Assessor*/
SA_DATE_NOVAL_TRANSFER INT, /*Date of the last recorded non-arms-length transfer without money, typically a quitclaim or other deed filed in the nature of a quitclaim.*/
SA_DOC_NBR_NOVAL VARCHAR(20), /*Document number of the last recorded non-arms-length transfer without money, typically a quitclaim or other deed filed in the nature of a quitclaim.*/
SA_INACTIVE_PARCEL_FLAG VARCHAR(1), /*Flag that indicates the property is no longer active, and will not be updated.*/
SA_SHELL_PARCEL_FLAG VARCHAR(1), /*Flag that indicates the property is a shell record, and a part of a parcel split.*/
'''
class_dict={}
factory_dict={}
am_dict=[]

for line in amenity_raw.split('\n'):
	line = line.split(' ')[0]
	am_dict.append(line)

for line in raw_attribute.split('\n'):
	line = line.strip()
	key = line.split('String')[1].split(';')[0].strip()
	class_dict[key] = line

for line in raw_fact.split('\n'):
	line = line.strip()
	value = line.split('rs,')[1].split(',')[0].strip()
	if value.startswith('"') and value.endswith('"'):
		value = value[1:-1]
	key = line.split('dqAssessor.')[1].split('=')[0].strip()
	factory_dict[key] = value

good = 0
bad = 0
toPrint=[]
for attrName,line in class_dict.items():
	if factory_dict.has_key(attrName):
		columnName = factory_dict.get(attrName)
		# amenity
		if columnName in am_dict:
			print "@RedshiftColumn(name=\"%s\", isAmenity=true, useColumnNameForAmenity=true)" %(columnName)
		# not amenity
		else:
			print "@RedshiftColumn(name=\"%s\")" %(columnName)
		print line
		print ""
		good +=1
	else:
		bad +=1
		toPrint.append(line)

for line in toPrint:
	print line
	print ""



