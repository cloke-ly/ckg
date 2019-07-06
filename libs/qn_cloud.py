from qiniu import Auth, put_file

from CKG import cfg


def upload_to_qn(filepath,upload_filename):
    qn_auth = Auth(cfg.QN_ACCESSKEY,cfg.QN_SECRETKEY)

    token = qn_auth.upload_token(cfg.QN_BUCKET,upload_filename,3600)

    ret,info = put_file(token,upload_filename,filepath)

    return (ret,info)