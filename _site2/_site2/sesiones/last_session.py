class Ultima_sesion:

    def obtain_token(self):
        if (bool(self.token) == False):
            #   #   Obtener la autenticacio del endpoint    #  #
            #access token url
            access_token_url = 'https://g6d5f1265b0dcaf-dbapex.adb.us-ashburn-1.oraclecloudapps.com/ords/db_apex/oauth/token'

            #client (application) credentials - located at apim.byu.edu
            client_id = 'VYBnKhKCD1mHbYfmDgmIOQ..'
            client_secret = 'u6Wkk7p4r2oj-IRtz84CjQ..'

            #authentication type
            token_req_payload = {'grant_type': 'client_credentials'}


            token_response = requests.post(access_token_url,
            data=token_req_payload, verify=False, allow_redirects=False,
            auth=(client_id, client_secret))


            if token_response.status_code != 200:
            	print("Failed to obtain token from the OAuth 2.0 server", file=sys.stderr)
            	sys.exit(1)

            ##
            ## 	obtain a token before calling the API for the first time
            ## 	the token is valid for 15 minutes
            ##

            print("Successfuly obtained a new token")
            tokens = json.loads(token_response.text)
            token = tokens['access_token']

            ##
            ##   call the API with the token
            ##
            api_call_headers = {'Authorization': 'Bearer ' + token}
            return api_call_headers
        else:
            return self.token


    def get_last_session_id(self,api_call_headers):

      #    #    #    #     OBTENER EL ID DE LA SESION DE ENTRENAMIENTO     #    #   #  #
          url_ultima_sesion_entrenamiento = "https://g6d5f1265b0dcaf-dbapex.adb.us-ashburn-1.oraclecloudapps.com/ords/db_apex/sesion/last_sesion"

          api_call_sesion_response = requests.get(url_ultima_sesion_entrenamiento, headers=api_call_headers,verify=False)


          if	api_call_sesion_response.status_code == 401:
            token = get_new_token()
          else:

              id_sesion_json = api_call_sesion_response.json()


          sesion_id_num = (int) (id_sesion_json['items'][0]['sesion_entrenamiento_id'])
          print(sesion_id_num)

          return sesion_id_num

    def get_last_session_wimu_info(self,api_call_headers):

    #    #    #    #     OBTENER EL ID DE LA SESION DE ENTRENAMIENTO     #    #   #  #
        url_ultima_sesion_entrenamiento = "https://g6d5f1265b0dcaf-dbapex.adb.us-ashburn-1.oraclecloudapps.com/ords/db_apex/sesion/last_sesion_wimu_data"

        api_call_sesion_response = requests.get(url_ultima_sesion_entrenamiento, headers=api_call_headers,verify=False)


        if	api_call_sesion_response.status_code == 401:
          token = get_new_token()
        else:
            data = api_call_sesion_response.json()

        return data
