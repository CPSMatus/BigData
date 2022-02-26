BEGIN

OAUTH.create_client(
    p_name => 'client_one',
    p_grant_type      => 'client_credentials',
    p_owner           => 'DB_APEX',
    p_description     => 'Creating client for REST API GET authentication',
    p_support_email   => 'smatus@clubpuebla.com',
    p_privilege_names => 'customer_api_priv'
);

OAUTH.grant_client_role(
    p_client_name => 'client_one',
    p_role_name => 'customer_api_rol'

);

COMMIT;
END;
