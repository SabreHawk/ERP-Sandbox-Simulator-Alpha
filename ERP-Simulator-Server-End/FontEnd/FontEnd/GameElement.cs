using System;
using System.Collections;
using System.Collections.Generic;
using System.Text;
using Newtonsoft.Json;
namespace FontEnd {
    class GameElementList {
    }

    class CompanyInfo {
        int initialCash;
        int managementFee;

        public CompanyInfo(int _iC, int _mF) {
            InitialCash = _iC;
            ManagementFee = _mF;
        }
        public CompanyInfo(String _jsonInfo) {
            CompanyInfo tmp_cF = JsonConvert.DeserializeObject<CompanyInfo>(_jsonInfo);
            InitialCash = tmp_cF.InitialCash;
            ManagementFee = tmp_cF.ManagementFee;
        }

        public int InitialCash { get => initialCash; set => initialCash = value; }
        public int ManagementFee { get => managementFee; set => managementFee = value; }

        public String JsonSerialization() {
            return JsonConvert.SerializeObject(this);
        }
    }

    class LoanInfo {
        String name;
        int repayInterval;
        int repayTime;
        float interestRate;
        int loanLimitTimes;
        public LoanInfo(String _n, int _rI, int _rT, float _iR, int _lLT) {
            Name = _n;
            RepayInterval = _rI;
            RepayTime = _rT;
            InterestRate = _iR;
            LoanLimitTimes = _lLT;
        }
        public LoanInfo(String _jsonInfo) {
            LoanInfo tmp_info = JsonConvert.DeserializeObject<LoanInfo>(_jsonInfo);
            Name = tmp_info.Name;
            RepayInterval = tmp_info.RepayInterval;
            RepayTime = tmp_info.RepayTime;
            InterestRate = tmp_info.InterestRate;
            LoanLimitTimes = tmp_info.LoanLimitTimes;
        }

        public string Name { get => name; set => name = value; }
        public int RepayInterval { get => repayInterval; set => repayInterval = value; }
        public int RepayTime { get => repayTime; set => repayTime = value; }
        public float InterestRate { get => interestRate; set => interestRate = value; }
        public int LoanLimitTimes { get => loanLimitTimes; set => loanLimitTimes = value; }

        public String JsonSerialization() {
            return JsonConvert.SerializeObject(this);
        }
    }

    class FactoryInfo {
        String name;
        int purchaseCost;
        int capacity;
        int rentCost;
        int ownership;
        int area;
        int constructionTime;
        float depreciationRate;
        int rent2PurchaseCost;

        public FactoryInfo(String _n, int _c, int _r, int _o, int _a, int _cT, int _dR, int _rpC) {
            Name = _n;
            PurchaseCost = _c;
            RentCost = _r;
            Ownership = _o;
            Area = _a;
            ConstructionTime = _cT;
            depreciationRate = _dR;
            Rent2purchaseCost = _rpC;
        }
        public FactoryInfo(String _jsonInfo) {
            FactoryInfo tmpInfo = JsonConvert.DeserializeObject<FactoryInfo>(_jsonInfo);
            Name = tmpInfo.Name;
            PurchaseCost = tmpInfo.PurchaseCost;
            RentCost = tmpInfo.RentCost;
            Ownership = tmpInfo.Ownership;
            Area = tmpInfo.Area;
            ConstructionTime = tmpInfo.ConstructionTime;
            depreciationRate = tmpInfo.DepreciationRate;
            rent2PurchaseCost = tmpInfo.rent2PurchaseCost;
        }
        public string Name { get => name; set => name = value; }
        public int PurchaseCost { get => purchaseCost; set => purchaseCost = value; }
        public int Capacity { get => capacity; set => capacity = value; }
        public int RentCost { get => rentCost; set => rentCost = value; }
        public int Ownership { get => ownership; set => ownership = value; }
        public int Area { get => area; set => area = value; }
        public int ConstructionTime { get => constructionTime; set => constructionTime = value; }
        public float DepreciationRate { get => depreciationRate; set => depreciationRate = value; }
        public int Rent2purchaseCost { get => rent2PurchaseCost; set => rent2PurchaseCost = value; }

        public String JsonSerialization() {
            return JsonConvert.SerializeObject(this);
        }
    }

    class ProductionLineInfo {
        String name;
        int constructionTime;
        int constuctionCost;
        int rentCost;
        float depreciationRate;
        int maintainCost;
        int productivity;
        bool isTransfer;
        int transferTime;
        int transferCost;

        public ProductionLineInfo(String _n, int _cT, int _cC, int _rC, int _dR, int _mC, int _p,bool _iT, int _tT, int _tC) {
            Name = _n;
            ConstructionTime = _cT;
            ConstuctionCost = _cC;
            RentCost = _rC;
            DepreciationRate = _dR;
            MaintainCost = _mC;
            Productivity = _p;
            IsTransfer = _iT;
            TransferTime = _tT;
            TransferCost = _tC;
        }

        public ProductionLineInfo(String _jsonInfo) {
            ProductionLineInfo tmpInfo = JsonConvert.DeserializeObject<ProductionLineInfo>(_jsonInfo);
            Name = tmpInfo.Name;
            ConstructionTime = tmpInfo.ConstructionTime;
            ConstuctionCost = tmpInfo.ConstuctionCost;
            RentCost = tmpInfo.RentCost;
            DepreciationRate = tmpInfo.DepreciationRate;
            MaintainCost = tmpInfo.MaintainCost;
            Productivity = tmpInfo.Productivity;
            IsTransfer = tmpInfo.IsTransfer;
            TransferTime = tmpInfo.TransferTime;
            TransferCost = tmpInfo.TransferCost;
        }

        public string Name { get => name; set => name = value; }
        public int ConstructionTime { get => constructionTime; set => constructionTime = value; }
        public int ConstuctionCost { get => constuctionCost; set => constuctionCost = value; }
        public int RentCost { get => rentCost; set => rentCost = value; }
        public float DepreciationRate { get => depreciationRate; set => depreciationRate = value; }
        public int MaintainCost { get => maintainCost; set => maintainCost = value; }
        public int Productivity { get => productivity; set => productivity = value; }
        public int TransferTime { get => transferTime; set => transferTime = value; }
        public int TransferCost { get => transferCost; set => transferCost = value; }
        public bool IsTransfer { get => isTransfer; set => isTransfer = value; }

        public String JsonSerialization() {
            return JsonConvert.SerializeObject(this);
        }
    }

    class RawMaterialInfo {
        String name;
        int price;
        int transportTime;
        int emgPurchaseTimes;
        float discoutRate;

        public RawMaterialInfo(String _n, int _p, int _tT, int _ePT, int _dT) {
            Name = _n;
            Price = _p;
            TransportTime = _tT;
            EmgPurchaseTimes = _ePT;
            DiscoutRate = _dT;
        }

        public RawMaterialInfo(String _jsonInfo) {
            RawMaterialInfo tmpInfo = JsonConvert.DeserializeObject<RawMaterialInfo>(_jsonInfo);
            Name = tmpInfo.Name;
            Price = tmpInfo.Price;
            EmgPurchaseTimes = tmpInfo.EmgPurchaseTimes;
            DiscoutRate = tmpInfo.DiscoutRate;
        }
        public string Name { get => name; set => name = value; }
        public int Price { get => price; set => price = value; }
        public int TransportTime { get => transportTime; set => transportTime = value; }
        public int EmgPurchaseTimes { get => emgPurchaseTimes; set => emgPurchaseTimes = value; }
        public float DiscoutRate { get => discoutRate; set => discoutRate = value; }

        public String JsonSerialization() {
            return JsonConvert.SerializeObject(this);
        }
    }

    class ProductionInfo {
        String name;
        Hashtable formula;
        int price;
        int emgPurchaseTimes;
        int developTime;
        float discountRate;

        public ProductionInfo(String _n, Hashtable _f, int _p, int _e, int _dT, int _dR) {
            Name = _n;
            Formula = _f;
            Price = _p;
            EmgPurchaseTimes = _e;
            DevelopTime = _dT;
            DiscountRate = _dR;
        }



        public ProductionInfo(String _jsonInfo) {
            ProductionInfo tmpInfo = JsonConvert.DeserializeObject<ProductionInfo>(_jsonInfo);
            Name = tmpInfo.Name;
            Formula = tmpInfo.Formula;
            Price = tmpInfo.Price;
            EmgPurchaseTimes = tmpInfo.EmgPurchaseTimes;
            DevelopTime = tmpInfo.DevelopTime;
            DiscountRate = tmpInfo.DiscountRate;
        }

        public string Name { get => name; set => name = value; }
        public Hashtable Formula { get => formula; set => formula = value; }
        public int Price { get => price; set => price = value; }
        public int EmgPurchaseTimes { get => emgPurchaseTimes; set => emgPurchaseTimes = value; }
        public int DevelopTime { get => developTime; set => developTime = value; }
        public float DiscountRate { get => discountRate; set => discountRate = value; }
            
        public String JsonSerialization() {
            return JsonConvert.SerializeObject(this);
        }
    }

    class ProductionCertificationInfo {
        String name;
        int certTime;
        int certCost;
        public ProductionCertificationInfo(String _n,int _cT,int _cC) {
            Name = _n;
            CertTime = _cT;
            CertCost = _cC;
        }

        public ProductionCertificationInfo(String _jsonInfo) {
            ProductionCertificationInfo tmpInfo = JsonConvert.DeserializeObject<ProductionCertificationInfo>(_jsonInfo);
            Name = tmpInfo.Name;
            CertTime = tmpInfo.CertTime;
            CertCost = tmpInfo.CertCost;
        }
        public string Name { get => name; set => name = value; }
        public int CertTime { get => certTime; set => certTime = value; }
        public int CertCost { get => certCost; set => certCost = value; }

        public String JsonSerialization() {
            return JsonConvert.SerializeObject(this);
        }
    }


    class GameDate {
        int[] DAYS = { 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31 };
        int year;
        int month;
        int day;
        int hour;
        int minute;
        bool isIllegal;
        public GameDate(int _y, int _m, int _d, int _h, int _min) {
            isIllegal = false;
            Year = _y;
            Month = _m;
            Day = _d;
            Hour = _h;
            Minute = _min;
        }

        public int Year {
            get => year;
            set {
                if (value > 1000 && value < 10000) {
                    year = value;
                } else {
                    isIllegal = false;
                }
            }

        }
        public int Month {
            get => month;
            set {
                if (value > 0 && value < 13) {
                    month = value;
                } else {
                    isIllegal = false;
                }
            }
        }
        public int Day {
            get => day;
            set {
                bool isGap = (Year % 4 == 0 && Year % 100 == 0) || (Year % 400 == 0);
                int endDay = DAYS[Month];
                if (Month == 2 && isGap) {
                    endDay = 29;
                }
                if (value > 0 && value <= endDay) {
                    day = value;
                } else {
                    isIllegal = false;
                }
            }
        }
        public int Hour {
            get => hour;
            set {
                if (value > 0 && value < 13) {
                    hour = value;
                } else {
                    isIllegal = false;
                }
            }
        }
        public int Minute {
            get => minute;
            set {
                if (value >= 0 && value < 60) {
                    minute = value;
                } else {
                    isIllegal = false;
                }
            }
        }
        public override string ToString() {
            return Year.ToString() + "-" + Month.ToString() + "-" + Day.ToString() + "-" + Hour + ":" + Minute;     
        }
    }
    class GameInfo {
        String gameName;
        GameDate startDate;
        int maxPlayer;
        bool isPwd;
        String enrollPwd;
        GameDate enrollStartTime;
        GameDate enrollEndTime;

        public GameInfo(String _gN,GameDate _sD,int _mP,bool _iP,String _eP,GameDate _eST,GameDate _eET) {
            GameName = _gN;
            StartDate = _sD;
            MaxPlayer = _mP;
            IsPwd = _iP;
            EnrollPwd = _eP;
            EnrollStartTime = _eST;
            EnrollEndTime = _eET;
        }

        public GameInfo(String _jsonInfo) {
            GameInfo tmpInfo = JsonConvert.DeserializeObject<GameInfo>(_jsonInfo);
            GameName = tmpInfo.GameName;
            StartDate = tmpInfo.StartDate;
            MaxPlayer = tmpInfo.MaxPlayer;
            IsPwd = tmpInfo.IsPwd;
            EnrollPwd = tmpInfo.EnrollPwd;
            EnrollStartTime = tmpInfo.EnrollStartTime;
            EnrollEndTime = tmpInfo.EnrollEndTime;
        }

        public string GameName { get => gameName; set => gameName = value; }
        public GameDate StartDate { get => startDate; set => startDate = value; }
        public int MaxPlayer { get => maxPlayer; set => maxPlayer = value; }
        public bool IsPwd { get => isPwd; set => isPwd = value; }
        public string EnrollPwd { get => enrollPwd; set => enrollPwd = value; }
        public GameDate EnrollStartTime { get => enrollStartTime; set => enrollStartTime = value; }
        public GameDate EnrollEndTime { get => enrollEndTime; set => enrollEndTime = value; }

        public String JsonSerialization() {
            return JsonConvert.SerializeObject(this);
        }
    }
}
