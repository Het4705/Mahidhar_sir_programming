```mermaid
graph LR;
    A[Customers] -->|Registration/Login| B(User Management);
    B -->|Website Builder| C(Website Builder);
    B -->|Product Management| D(Product Management);
    B -->|Database Management| E(Database Management);
    B -->|Analytics| F(Analytics);
    B -->|Content Management| G(Content Management);

    C -->|Template Selection| D;
    D -->|Customization| E;
    E -->|Content Addition| F;
    F -->|Product Integration| G;
    G -->|Preview/Publish| H(Web Server);
    H -->|Published Website| WebServer;

    D -->|Product Addition| D;
    D -->|Product Editing| D;
    D -->|Product Deletion| D;
    D -->|Inventory Management| D;
    D -->|Image/Media Upload| D;
    D -->|Product Database| I(Product Database);

    F -->|Data Collection| F;
    F -->|Data Processing| F;
    F -->|Reporting| F;
    F -->|Customer Activity| A;
    F -->|Product Interaction| D;
    F -->|Analytics Reports| C;

    <!-- subgraph UserManagement;
        B1(Customer Registration) --> B2(Secure Customer Database);
        B3(Customer Login) --> B4(Authentication Module);
        B5(Shopkeeper Registration) --> B6(Secure Shopkeeper Database);
        B7(Shopkeeper Login) --> B8(Authentication Module);
        B9(Password Reset) --> B10(Verification/New Password) --> B2/B6;
    end;

    subgraph DatabaseManagement;
        E --> I;
        E --> J(Shopkeeper 1 Database);
        E --> K(Shopkeeper 2 Database);
        E --> L(Shopkeeper 3 Database);
        E --> M(Shopkeeper 4 Database);
        E --> N(Shopkeeper 5 Database);
        E --> O(Shopkeeper 6 Database);
        E --> P(Shopkeeper 7 Database);
        E --> Q(Shopkeeper 8 Database);
        E --> R(Shopkeeper 9 Database);
        E --> S(Shopkeeper 10 Database);
        E --> T(Shopkeeper 11 Database);
        E --> U(Shopkeeper 12 Database);
        E --> V(Shopkeeper 13 Database);
        E --> W(Shopkeeper 14 Database);
        E --> X(Shopkeeper 15 Database);
        E --> Y(Shopkeeper 16 Database);
        E --> Z(Shopkeeper 17 Database);
    end;

    subgraph AnalyticsReports;
        F --> C (Website Performance);
        F --> D (Sales Trends);
        F --> A (Customer Behavior);
    end; -->
