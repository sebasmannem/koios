//Copied from http://rest.elkstein.org/2008/02/using-rest-in-c-sharp.html

static string HttpGet(string url) {
  HttpWebRequest req = WebRequest.Create(url)
                       as HttpWebRequest;
  string result = null;
  using (HttpWebResponse resp = req.GetResponse()
                                as HttpWebResponse)
  {
    StreamReader reader =
        new StreamReader(resp.GetResponseStream());
    result = reader.ReadToEnd();
  }
  return result;
}

//Copied from http://rest.elkstein.org/2008/02/using-rest-in-c-sharp.html

static string HttpPost(string url, 
    string[] paramName, string[] paramVal)
{
  HttpWebRequest req = WebRequest.Create(new Uri(url)) 
                       as HttpWebRequest;
  req.Method = "POST";  
  req.ContentType = "application/x-www-form-urlencoded";

  // Build a string with all the params, properly encoded.
  // We assume that the arrays paramName and paramVal are
  // of equal length:
  StringBuilder paramz = new StringBuilder();
  for (int i = 0; i < paramName.Length; i++) {
    paramz.Append(paramName[i]);
    paramz.Append("=");
    paramz.Append(HttpUtility.UrlEncode(paramVal[i]));
    paramz.Append("&");
  }

  // Encode the parameters as form data:
  byte[] formData =
      UTF8Encoding.UTF8.GetBytes(paramz.ToString());
  req.ContentLength = formData.Length;

  // Send the request:
  using (Stream post = req.GetRequestStream())  
  {  
    post.Write(formData, 0, formData.Length);  
  }

  // Pick up the response:
  string result = null;
  using (HttpWebResponse resp = req.GetResponse()
                                as HttpWebResponse)  
  {  
    StreamReader reader = 
        new StreamReader(resp.GetResponseStream());
    result = reader.ReadToEnd();
  }

  return result;
}
