<!DOCTYPE html>
<!-- saved from url=(0073)https://colab.research.google.com/drive/1UQ9tc9AaVNd7WtJUnMArlHDBSayfozb8 -->
<html lang="en" theme="adaptive" editor="Default Light"><head><meta http-equiv="Content-Type" content="text/html; charset=UTF-8"><meta http-equiv="origin-trial" content="Az520Inasey3TAyqLyojQa8MnmCALSEU29yQFW8dePZ7xQTvSt73pHazLFTK5f7SyLUJSo2uKLesEtEa9aUYcgMAAACPeyJvcmlnaW4iOiJodHRwczovL2dvb2dsZS5jb206NDQzIiwiZmVhdHVyZSI6IkRpc2FibGVUaGlyZFBhcnR5U3RvcmFnZVBhcnRpdGlvbmluZyIsImV4cGlyeSI6MTcyNTQwNzk5OSwiaXNTdWJkb21haW4iOnRydWUsImlzVGhpcmRQYXJ0eSI6dHJ1ZX0="><meta http-equiv="origin-trial" content="Az520Inasey3TAyqLyojQa8MnmCALSEU29yQFW8dePZ7xQTvSt73pHazLFTK5f7SyLUJSo2uKLesEtEa9aUYcgMAAACPeyJvcmlnaW4iOiJodHRwczovL2dvb2dsZS5jb206NDQzIiwiZmVhdHVyZSI6IkRpc2FibGVUaGlyZFBhcnR5U3RvcmFnZVBhcnRpdGlvbmluZyIsImV4cGlyeSI6MTcyNTQwNzk5OSwiaXNTdWJkb21haW4iOnRydWUsImlzVGhpcmRQYXJ0eSI6dHJ1ZX0="><script type="text/javascript" async="" charset="utf-8" src="./Task 1 - Chatbot with Rule-based responses_files/recaptcha__en.js.download" crossorigin="anonymous" integrity="sha384-1qCnjZ4tqdtwUnG8/biz1OfJ7vkM3jnPZ0W0wIcDu+NDwZyQHqHpscJVB8ezdlTM" nonce=""></script><script type="text/javascript" async="" charset="utf-8" src="./Task 1 - Chatbot with Rule-based responses_files/recaptcha__en.js.download" crossorigin="anonymous" integrity="sha384-1qCnjZ4tqdtwUnG8/biz1OfJ7vkM3jnPZ0W0wIcDu+NDwZyQHqHpscJVB8ezdlTM" nonce=""></script><script type="text/javascript" async="" src="./Task 1 - Chatbot with Rule-based responses_files/js" nonce=""></script><script src="./Task 1 - Chatbot with Rule-based responses_files/cb=gapi.loaded_1" nonce="" async=""></script><script src="./Task 1 - Chatbot with Rule-based responses_files/cb=gapi.loaded_0" nonce="" async=""></script><script async="" src="./Task 1 - Chatbot with Rule-based responses_files/analytics.js.download"></script><script nonce="">
      document.addEventListener('keydown', (e) => {
        // Stop propagation on ESC because otherwise it will halt outbound XHRs
        // See b/131755324 for more info.
        if (e.key === 'Escape') {
          e.stopPropagation();
          e.preventDefault();
        }
      });
    </script><meta name="referrer" content="origin"><meta name="viewport" content="width=device-width, initial-scale=1"><title>Task 1 - Chatbot with Rule-based responses - Colab</title><link href="./Task 1 - Chatbot with Rule-based responses_files/css2" rel="stylesheet"><link href="./Task 1 - Chatbot with Rule-based responses_files/css" rel="stylesheet"><link rel="search" type="application/opensearchdescription+xml" href="https://colab.research.google.com/opensearch.xml" title="Google Colab"><style>.gb_8a:not(.gb_ad){font:13px/27px Roboto,Arial,sans-serif;z-index:986}@-webkit-keyframes gb__a{0%{opacity:0}50%{opacity:1}}@keyframes gb__a{0%{opacity:0}50%{opacity:1}}a.gb_qa{border:none;color:#4285f4;cursor:default;font-weight:bold;outline:none;position:relative;text-align:center;text-decoration:none;text-transform:uppercase;white-space:nowrap;-webkit-user-select:none}a.gb_qa:hover:after,a.gb_qa:focus:after{background-color:rgba(0,0,0,.12);content:"";height:100%;left:0;position:absolute;top:0;width:100%}a.gb_qa:hover,a.gb_qa:focus{text-decoration:none}a.gb_qa:active{background-color:rgba(153,153,153,.4);text-decoration:none}a.gb_ra{background-color:#4285f4;color:#fff}a.gb_ra:active{background-color:#0043b2}.gb_sa{box-shadow:0 1px 1px rgba(0,0,0,.16)}.gb_qa,.gb_ra,.gb_ta,.gb_ua{display:inline-block;line-height:28px;padding:0 12px;border-radius:2px}.gb_ta{background:#f8f8f8;border:1px solid #c6c6c6}.gb_ua{background:#f8f8f8}.gb_ta,#gb a.gb_ta.gb_ta,.gb_ua{color:#666;cursor:default;text-decoration:none}#gb a.gb_ua{cursor:default;text-decoration:none}.gb_ua{border:1px solid #4285f4;font-weight:bold;outline:none;background:#4285f4;background:-webkit-gradient(linear,left top,left bottom,from(top),color-stop(#4387fd),to(#4683ea));background:-webkit-linear-gradient(top,#4387fd,#4683ea);background:linear-gradient(top,#4387fd,#4683ea);filter:progid:DXImageTransform.Microsoft.gradient(startColorstr=#4387fd,endColorstr=#4683ea,GradientType=0)}#gb a.gb_ua{color:#fff}.gb_ua:hover{box-shadow:0 1px 0 rgba(0,0,0,.15)}.gb_ua:active{box-shadow:inset 0 2px 0 rgba(0,0,0,.15);background:#3c78dc;background:-webkit-gradient(linear,left top,left bottom,from(top),color-stop(#3c7ae4),to(#3f76d3));background:-webkit-linear-gradient(top,#3c7ae4,#3f76d3);background:linear-gradient(top,#3c7ae4,#3f76d3);filter:progid:DXImageTransform.Microsoft.gradient(startColorstr=#3c7ae4,endColorstr=#3f76d3,GradientType=0)}#gb .gb_va{background:#fff;border:1px solid #dadce0;color:#1a73e8;display:inline-block;text-decoration:none}#gb .gb_va:hover{background:#f8fbff;border-color:#dadce0;color:#174ea6}#gb .gb_va:focus{background:#f4f8ff;color:#174ea6;outline:1px solid #174ea6}#gb .gb_va:active,#gb .gb_va:focus:active{background:#ecf3fe;color:#174ea6}#gb .gb_va.gb_i{background:transparent;border:1px solid #5f6368;color:#8ab4f8;text-decoration:none}#gb .gb_va.gb_i:hover{background:rgba(255,255,255,.04);color:#e8eaed}#gb .gb_va.gb_i:focus{background:rgba(232,234,237,.12);color:#e8eaed;outline:1px solid #e8eaed}#gb .gb_va.gb_i:active,#gb .gb_va.gb_i:focus:active{background:rgba(232,234,237,.1);color:#e8eaed}.gb_Fd{display:inline-block;vertical-align:middle}.gb_Id .gb_q{bottom:-3px;right:-5px}.gb_f{position:relative}.gb_d{display:inline-block;outline:none;vertical-align:middle;border-radius:2px;box-sizing:border-box;height:40px;width:40px;cursor:pointer;text-decoration:none}#gb#gb a.gb_d{cursor:pointer;text-decoration:none}.gb_d,a.gb_d{color:#000}.gb_4e{border-color:transparent;border-bottom-color:#fff;border-style:dashed dashed solid;border-width:0 8.5px 8.5px;display:none;position:absolute;left:11.5px;top:33px;z-index:1;height:0;width:0;-webkit-animation:gb__a .2s;animation:gb__a .2s}.gb_5e{border-color:transparent;border-style:dashed dashed solid;border-width:0 8.5px 8.5px;display:none;position:absolute;left:11.5px;z-index:1;height:0;width:0;-webkit-animation:gb__a .2s;animation:gb__a .2s;border-bottom-color:rgba(0,0,0,.2);top:32px}x:-o-prefocus,div.gb_5e{border-bottom-color:#ccc}.gb_V{background:#fff;border:1px solid #ccc;border-color:rgba(0,0,0,.2);color:#000;-webkit-box-shadow:0 2px 10px rgba(0,0,0,.2);box-shadow:0 2px 10px rgba(0,0,0,.2);display:none;outline:none;overflow:hidden;position:absolute;right:8px;top:62px;-webkit-animation:gb__a .2s;animation:gb__a .2s;border-radius:2px;-webkit-user-select:text}.gb_Fd.gb_Da .gb_4e,.gb_Fd.gb_Da .gb_5e,.gb_Fd.gb_Da .gb_V,.gb_Da.gb_V{display:block}.gb_Fd.gb_Da.gb_6e .gb_4e,.gb_Fd.gb_Da.gb_6e .gb_5e{display:none}.gb_Jd{position:absolute;right:8px;top:62px;z-index:-1}.gb_Za .gb_4e,.gb_Za .gb_5e,.gb_Za .gb_V{margin-top:-10px}.gb_Fd:first-child,#gbsfw:first-child+.gb_Fd{padding-left:4px}.gb_ga.gb_Kd .gb_Fd:first-child{padding-left:0}.gb_Ld{position:relative}.gb_Wc .gb_Ld,.gb_cd .gb_Ld{float:right}.gb_d{padding:8px;cursor:pointer}.gb_d:after{content:"";position:absolute;top:-4px;bottom:-4px;left:-4px;right:-4px}.gb_ga .gb_9d:not(.gb_qa):focus img{background-color:rgba(0,0,0,.2);outline:none;-webkit-border-radius:50%;border-radius:50%}.gb_Md button svg,.gb_d{-webkit-border-radius:50%;border-radius:50%}.gb_Md button:focus:not(:focus-visible) svg,.gb_Md button:hover svg,.gb_Md button:active svg,.gb_d:focus:not(:focus-visible),.gb_d:hover,.gb_d:active,.gb_d[aria-expanded=true]{outline:none}.gb_Fc .gb_Md.gb_ie button:focus-visible svg,.gb_Md button:focus-visible svg,.gb_d:focus-visible{outline:1px solid #202124}.gb_Fc .gb_Md button:focus-visible svg,.gb_Fc .gb_d:focus-visible{outline:1px solid #f1f3f4}@media (forced-colors:active){.gb_Fc .gb_Md.gb_ie button:focus-visible svg,.gb_Md button:focus-visible svg,.gb_Fc .gb_Md button:focus-visible svg{outline:1px solid currentcolor}}.gb_Fc .gb_Md.gb_ie button:focus svg,.gb_Fc .gb_Md.gb_ie button:focus:hover svg,.gb_Md button:focus svg,.gb_Md button:focus:hover svg,.gb_d:focus,.gb_d:focus:hover{background-color:rgba(60,64,67,.1)}.gb_Fc .gb_Md.gb_ie button:active svg,.gb_Md button:active svg,.gb_d:active{background-color:rgba(60,64,67,.12)}.gb_Fc .gb_Md.gb_ie button:hover svg,.gb_Md button:hover svg,.gb_d:hover{background-color:rgba(60,64,67,.08)}.gb_wa .gb_d.gb_ya:hover{background-color:transparent}.gb_d[aria-expanded=true],.gb_d:hover[aria-expanded=true]{background-color:rgba(95,99,104,.24)}.gb_d[aria-expanded=true] .gb_h{fill:#5f6368;opacity:1}.gb_Fc .gb_Md button:hover svg,.gb_Fc .gb_d:hover{background-color:rgba(232,234,237,.08)}.gb_Fc .gb_Md button:focus svg,.gb_Fc .gb_Md button:focus:hover svg,.gb_Fc .gb_d:focus,.gb_Fc .gb_d:focus:hover{background-color:rgba(232,234,237,.1)}.gb_Fc .gb_Md button:active svg,.gb_Fc .gb_d:active{background-color:rgba(232,234,237,.12)}.gb_Fc .gb_d[aria-expanded=true],.gb_Fc .gb_d:hover[aria-expanded=true]{background-color:rgba(255,255,255,.12)}.gb_Fc .gb_d[aria-expanded=true] .gb_h{fill:#fff;opacity:1}.gb_Fd{padding:4px}.gb_ga.gb_Kd .gb_Fd{padding:4px 2px}.gb_ga.gb_Kd .gb_b.gb_Fd{padding-left:6px}.gb_V{z-index:991;line-height:normal}.gb_V.gb_Nd{left:0;right:auto}@media (max-width:350px){.gb_V.gb_Nd{left:0}}.gb_Od .gb_V{top:56px}.gb_m{display:none!important}.gb_Sa{visibility:hidden}.gb_k .gb_d,.gb_U .gb_k .gb_d{background-position:-64px -29px}.gb_A .gb_k .gb_d{background-position:-29px -29px;opacity:1}.gb_k .gb_d,.gb_k .gb_d:hover,.gb_k .gb_d:focus{opacity:1}.gb_n{display:none}@media screen and (max-width:319px){.gb_id:not(.gb_od) .gb_k{display:none;visibility:hidden}}.gb_q{display:none}.gb_5c{font-family:Google Sans,Roboto,Helvetica,Arial,sans-serif;font-size:20px;font-weight:400;letter-spacing:0.25px;line-height:48px;margin-bottom:2px;opacity:1;overflow:hidden;padding-left:16px;position:relative;text-overflow:ellipsis;vertical-align:middle;top:2px;white-space:nowrap;-webkit-flex:1 1 auto;-webkit-box-flex:1;flex:1 1 auto}.gb_5c.gb_6c{color:#3c4043}.gb_ga.gb_Ia .gb_5c{margin-bottom:0}.gb_7c.gb_8c .gb_5c{padding-left:4px}.gb_ga.gb_Ia .gb_9c{position:relative;top:-2px}.gb_ga{color:black;min-width:160px;position:relative;-webkit-transition:box-shadow 250ms;transition:box-shadow 250ms}.gb_ga.gb_Oc{min-width:120px}.gb_ga.gb_gd .gb_hd{display:none}.gb_ga.gb_gd .gb_id{height:56px}header.gb_ga{display:block}.gb_ga svg{fill:currentColor}.gb_jd{position:fixed;top:0;width:100%}.gb_kd{-webkit-box-shadow:0 4px 5px 0 rgba(0,0,0,.14),0 1px 10px 0 rgba(0,0,0,.12),0 2px 4px -1px rgba(0,0,0,.2);box-shadow:0 4px 5px 0 rgba(0,0,0,.14),0 1px 10px 0 rgba(0,0,0,.12),0 2px 4px -1px rgba(0,0,0,.2)}.gb_ld{height:64px}.gb_id{-webkit-box-sizing:border-box;box-sizing:border-box;position:relative;width:100%;display:-webkit-box;display:-webkit-flex;display:flex;-webkit-box-pack:space-between;-webkit-justify-content:space-between;justify-content:space-between;min-width:-webkit-min-content;min-width:min-content}.gb_ga:not(.gb_Ia) .gb_id{padding:8px}.gb_ga.gb_nd .gb_id{-webkit-flex:1 0 auto;-webkit-box-flex:1;flex:1 0 auto}.gb_ga .gb_id.gb_od.gb_pd{min-width:0}.gb_ga.gb_Ia .gb_id{padding:4px;padding-left:8px;min-width:0}.gb_hd{height:48px;vertical-align:middle;white-space:nowrap;-webkit-box-align:center;-webkit-align-items:center;align-items:center;display:-webkit-box;display:-webkit-flex;display:flex;-webkit-user-select:none}.gb_rd>.gb_hd{display:table-cell;width:100%}.gb_7c{padding-right:30px;box-sizing:border-box;-webkit-flex:1 0 auto;-webkit-box-flex:1;flex:1 0 auto}.gb_ga.gb_Ia .gb_7c{padding-right:14px}.gb_sd{-webkit-flex:1 1 100%;-webkit-box-flex:1;flex:1 1 100%}.gb_sd>:only-child{display:inline-block}.gb_td.gb_Xc{padding-left:4px}.gb_td.gb_ud,.gb_ga.gb_nd .gb_td,.gb_ga.gb_Ia:not(.gb_cd) .gb_td{padding-left:0}.gb_ga.gb_Ia .gb_td.gb_ud{padding-right:0}.gb_ga.gb_Ia .gb_td.gb_ud .gb_wa{margin-left:10px}.gb_Xc{display:inline}.gb_ga.gb_Rc .gb_td.gb_vd,.gb_ga.gb_cd .gb_td.gb_vd{padding-left:2px}.gb_5c{display:inline-block}.gb_td{-webkit-box-sizing:border-box;box-sizing:border-box;height:48px;line-height:normal;padding:0 4px;padding-left:30px;-webkit-flex:0 0 auto;-webkit-box-flex:0;flex:0 0 auto;-webkit-box-pack:flex-end;-webkit-justify-content:flex-end;justify-content:flex-end}.gb_cd{height:48px}.gb_ga.gb_cd{min-width:auto}.gb_cd .gb_td{float:right;padding-left:32px}.gb_cd .gb_td.gb_wd{padding-left:0}.gb_xd{font-size:14px;max-width:200px;overflow:hidden;padding:0 12px;text-overflow:ellipsis;white-space:nowrap;-webkit-user-select:text}.gb_bd{-webkit-transition:background-color .4s;-webkit-transition:background-color .4s;transition:background-color .4s}.gb_Dd{color:black}.gb_Fc{color:white}.gb_ga a,.gb_Lc a{color:inherit}.gb_L{color:rgba(0,0,0,.87)}.gb_ga svg,.gb_Lc svg,.gb_7c .gb_fd,.gb_Wc .gb_fd{color:#5f6368;opacity:1}.gb_Fc svg,.gb_Lc.gb_Pc svg,.gb_Fc .gb_7c .gb_fd,.gb_Fc .gb_7c .gb_Ec,.gb_Fc .gb_7c .gb_9c,.gb_Lc.gb_Pc .gb_fd{color:rgba(255,255,255,.87)}.gb_Fc .gb_7c .gb_Dc:not(.gb_Ed){opacity:.87}.gb_6c{color:inherit;opacity:1;text-rendering:optimizeLegibility;-webkit-font-smoothing:antialiased}.gb_Fc .gb_6c,.gb_Dd .gb_6c{opacity:1}.gb_yd{position:relative}.gb_zd{font-family:arial,sans-serif;line-height:normal;padding-right:15px}a.gb_x,span.gb_x{color:rgba(0,0,0,.87);text-decoration:none}.gb_Fc a.gb_x,.gb_Fc span.gb_x{color:white}a.gb_x:focus{outline-offset:2px}a.gb_x:hover{text-decoration:underline}.gb_y{display:inline-block;padding-left:15px}.gb_y .gb_x{display:inline-block;line-height:24px;vertical-align:middle}.gb_dd{font-family:Google Sans,Roboto,Helvetica,Arial,sans-serif;font-weight:500;font-size:14px;letter-spacing:.25px;line-height:16px;margin-left:10px;margin-right:8px;min-width:96px;padding:9px 23px;text-align:center;vertical-align:middle;border-radius:4px;box-sizing:border-box}.gb_ga.gb_cd .gb_dd{margin-left:8px}#gb a.gb_ua.gb_dd{cursor:pointer}.gb_ua.gb_dd:hover{background:#1b66c9;-webkit-box-shadow:0 1px 3px 1px rgba(66,64,67,.15),0 1px 2px 0 rgba(60,64,67,.3);box-shadow:0 1px 3px 1px rgba(66,64,67,.15),0 1px 2px 0 rgba(60,64,67,.3)}.gb_ua.gb_dd:focus,.gb_ua.gb_dd:hover:focus{background:#1c5fba;-webkit-box-shadow:0 1px 3px 1px rgba(66,64,67,.15),0 1px 2px 0 rgba(60,64,67,.3);box-shadow:0 1px 3px 1px rgba(66,64,67,.15),0 1px 2px 0 rgba(60,64,67,.3)}.gb_ua.gb_dd:active{background:#1b63c1;-webkit-box-shadow:0 1px 3px 1px rgba(66,64,67,.15),0 1px 2px 0 rgba(60,64,67,.3);box-shadow:0 1px 3px 1px rgba(66,64,67,.15),0 1px 2px 0 rgba(60,64,67,.3)}.gb_dd{background:#1a73e8;border:1px solid transparent}.gb_ga.gb_Ia .gb_dd{padding:9px 15px;min-width:80px}.gb_Ad{text-align:left}#gb .gb_Fc a.gb_dd:not(.gb_i),#gb.gb_Fc a.gb_dd{background:#fff;border-color:#dadce0;-webkit-box-shadow:none;box-shadow:none;color:#1a73e8}#gb a.gb_ua.gb_i.gb_dd{background:#8ab4f8;border:1px solid transparent;-webkit-box-shadow:none;box-shadow:none;color:#202124}#gb .gb_Fc a.gb_dd:hover:not(.gb_i),#gb.gb_Fc a.gb_dd:hover{background:#f8fbff;border-color:#cce0fc}#gb a.gb_ua.gb_i.gb_dd:hover{background:#93baf9;border-color:transparent;-webkit-box-shadow:0 1px 3px 1px rgba(0,0,0,.15),0 1px 2px rgba(0,0,0,.3);box-shadow:0 1px 3px 1px rgba(0,0,0,.15),0 1px 2px rgba(0,0,0,.3)}#gb .gb_Fc a.gb_dd:focus:not(.gb_i),#gb .gb_Fc a.gb_dd:focus:hover:not(.gb_i),#gb.gb_Fc a.gb_dd:focus:not(.gb_i),#gb.gb_Fc a.gb_dd:focus:hover:not(.gb_i){background:#f4f8ff;outline:1px solid #c9ddfc}#gb a.gb_ua.gb_i.gb_dd:focus,#gb a.gb_ua.gb_i.gb_dd:focus:hover{background:#a6c6fa;border-color:transparent;-webkit-box-shadow:none;box-shadow:none}#gb .gb_Fc a.gb_dd:active:not(.gb_i),#gb.gb_Fc a.gb_dd:active{background:#ecf3fe}#gb a.gb_ua.gb_i.gb_dd:active{background:#a1c3f9;-webkit-box-shadow:0 1px 2px rgba(60,64,67,.3),0 2px 6px 2px rgba(60,64,67,.15);box-shadow:0 1px 2px rgba(60,64,67,.3),0 2px 6px 2px rgba(60,64,67,.15)}.gb_l{display:none}@media screen and (max-width:319px){.gb_id:not(.gb_od) .gb_k{display:none;visibility:hidden}}.gb_wa{background-color:rgba(255,255,255,.88);border:1px solid #dadce0;-webkit-box-sizing:border-box;box-sizing:border-box;cursor:pointer;display:inline-block;max-height:48px;overflow:hidden;outline:none;padding:0;vertical-align:middle;width:134px;-webkit-border-radius:8px;border-radius:8px}.gb_wa.gb_i{background-color:transparent;border:1px solid #5f6368}.gb_Ca{display:inherit}.gb_wa.gb_i .gb_Ca{background:#fff;-webkit-border-radius:4px;border-radius:4px;display:inline-block;left:8px;margin-right:5px;position:relative;padding:3px;top:-1px}.gb_wa:hover{border:1px solid #d2e3fc;background-color:rgba(248,250,255,.88)}.gb_wa.gb_i:hover{background-color:rgba(241,243,244,.04);border:1px solid #5f6368}.gb_wa:focus-visible,.gb_wa:focus{background-color:#fff;outline:1px solid #202124;-webkit-box-shadow:0 1px 2px 0 rgba(60,64,67,.3),0 1px 3px 1px rgba(60,64,67,.15);box-shadow:0 1px 2px 0 rgba(60,64,67,.3),0 1px 3px 1px rgba(60,64,67,.15)}.gb_wa.gb_i:focus-visible,.gb_wa.gb_i:focus{background-color:rgba(241,243,244,.12);outline:1px solid #f1f3f4;-webkit-box-shadow:0 1px 3px 1px rgba(0,0,0,.15),0 1px 2px 0 rgba(0,0,0,.3);box-shadow:0 1px 3px 1px rgba(0,0,0,.15),0 1px 2px 0 rgba(0,0,0,.3)}.gb_wa.gb_i:active,.gb_wa.gb_Da.gb_i:focus{background-color:rgba(241,243,244,.1);border:1px solid #5f6368}.gb_Ea{display:inline-block;padding-bottom:2px;padding-left:7px;padding-top:2px;text-align:center;vertical-align:middle;line-height:32px;width:78px}.gb_wa.gb_i .gb_Ea{line-height:26px;margin-left:0;padding-bottom:0;padding-left:0;padding-top:0;width:72px}.gb_Ea.gb_Fa{background-color:#f1f3f4;-webkit-border-radius:4px;border-radius:4px;margin-left:8px;padding-left:0;line-height:30px}.gb_Ea.gb_Fa .gb_Ha{vertical-align:middle}.gb_ga:not(.gb_Ia) .gb_wa{margin-left:10px;margin-right:4px}.gb_Ja{max-height:32px;width:78px}.gb_wa.gb_i .gb_Ja{max-height:26px;width:72px}.gb_p{-webkit-background-size:32px 32px;background-size:32px 32px;border:0;-webkit-border-radius:50%;border-radius:50%;display:block;margin:0px;position:relative;height:32px;width:32px;z-index:0}.gb_Ta{background-color:#e8f0fe;border:1px solid rgba(32,33,36,.08);position:relative}.gb_Ta.gb_p{height:30px;width:30px}.gb_Ta.gb_p:hover,.gb_Ta.gb_p:active{-webkit-box-shadow:none;box-shadow:none}.gb_Ua{background:#fff;border:none;-webkit-border-radius:50%;border-radius:50%;bottom:2px;-webkit-box-shadow:0px 1px 2px 0px rgba(60,64,67,.30),0px 1px 3px 1px rgba(60,64,67,.15);box-shadow:0px 1px 2px 0px rgba(60,64,67,.30),0px 1px 3px 1px rgba(60,64,67,.15);height:14px;margin:2px;position:absolute;right:0;width:14px}.gb_Va{color:#1f71e7;font:400 22px/32px Google Sans,Roboto,Helvetica,Arial,sans-serif;text-align:center;text-transform:uppercase}@media (-webkit-min-device-pixel-ratio:1.25),(min-resolution:1.25dppx),(min-device-pixel-ratio:1.25){.gb_p::before,.gb_Wa::before{display:inline-block;-webkit-transform:scale(0.5);-webkit-transform:scale(0.5);transform:scale(0.5);-webkit-transform-origin:left 0;-webkit-transform-origin:left 0;transform-origin:left 0}.gb_C .gb_Wa::before{-webkit-transform:scale(scale(0.416666667));-webkit-transform:scale(scale(0.416666667));transform:scale(scale(0.416666667))}}.gb_p:hover,.gb_p:focus{-webkit-box-shadow:0 1px 0 rgba(0,0,0,.15);box-shadow:0 1px 0 rgba(0,0,0,.15)}.gb_p:active{-webkit-box-shadow:inset 0 2px 0 rgba(0,0,0,.15);box-shadow:inset 0 2px 0 rgba(0,0,0,.15)}.gb_p:active::after{background:rgba(0,0,0,.1);-webkit-border-radius:50%;border-radius:50%;content:"";display:block;height:100%}.gb_Xa{cursor:pointer;line-height:40px;min-width:30px;opacity:.75;overflow:hidden;vertical-align:middle;text-overflow:ellipsis}.gb_d.gb_Xa{width:auto}.gb_Xa:hover,.gb_Xa:focus{opacity:.85}.gb_Za .gb_Xa,.gb_Za .gb_0a{line-height:26px}#gb#gb.gb_Za a.gb_Xa,.gb_Za .gb_0a{font-size:11px;height:auto}.gb_1a{border-top:4px solid #000;border-left:4px dashed transparent;border-right:4px dashed transparent;display:inline-block;margin-left:6px;opacity:.75;vertical-align:middle}.gb_ya:hover .gb_1a{opacity:.85}.gb_wa>.gb_b{padding:3px 3px 3px 4px}.gb_2a.gb_Sa{color:#fff}.gb_A .gb_Xa,.gb_A .gb_1a{opacity:1}#gb#gb.gb_A.gb_A a.gb_Xa,#gb#gb .gb_A.gb_A a.gb_Xa{color:#fff}.gb_A.gb_A .gb_1a{border-top-color:#fff;opacity:1}.gb_U .gb_p:hover,.gb_A .gb_p:hover,.gb_U .gb_p:focus,.gb_A .gb_p:focus{-webkit-box-shadow:0 1px 0 rgba(0,0,0,.15),0 1px 2px rgba(0,0,0,.2);box-shadow:0 1px 0 rgba(0,0,0,.15),0 1px 2px rgba(0,0,0,.2)}.gb_3a .gb_b,.gb_4a .gb_b{position:absolute;right:1px}.gb_b.gb_z,.gb_5a.gb_z,.gb_ya.gb_z{-webkit-flex:0 1 auto;-webkit-box-flex:0;flex:0 1 auto}.gb_6a.gb_7a .gb_Xa{width:30px!important}.gb_o{height:40px;position:absolute;right:-5px;top:-5px;width:40px}.gb_8a .gb_o,.gb_9a .gb_o{right:0;top:0}.gb_b .gb_d{padding:4px}.gb_r{display:none}sentinel{}</style><script nonce="">;this.gbar_={CONFIG:[[[0,"www.gstatic.com","og.qtm.en_US.k_rHrBjflTk.2019.O","co.in","en","425",0,[4,2,"","","","648210890","0"],null,"xZqLZvvIMJ67wN4PqYimmA4",null,0,"og.qtm.nuHTXYWlLd0.L.W.O","AA2YrTt1hnGqeS6CLgm_ywEWql2sJwW4iA","AA2YrTuab1saMfPg0iiAR9TwFTm87PY2ug","",2,1,200,"IND",null,null,"425","425",1,null,null,114591953,1],null,[1,0.1000000014901161,2,1],null,[1,0,0,null,"0","indlanithish2002@gmail.com","","ALumJKKU0BBNS3q5xO5UazenkCzcbC_bOnR7cXiHCn9APwJWMyZfDIho2tV2C-CcbxVuZNjMxD-1xSdB8UYtvlg4OSLzJAkevg",0,0,0],[0,0,"",1,0,0,0,0,0,0,null,0,0,null,0,0,null,null,0,0,0,"","","","","","",null,0,0,0,0,0,null,null,null,"rgba(32,33,36,1)","rgba(255,255,255,1)",0,0,0,null,null,1,0,0,null,0],["%1$s (default)","Brand account",1,"%1$s (delegated)",1,null,83,"https://colab.research.google.com/drive/1UQ9tc9AaVNd7WtJUnMArlHDBSayfozb8?authuser=$authuser",null,null,null,1,"https://accounts.google.com/ListAccounts?listPages=0\u0026pid=425\u0026gpsia=1\u0026source=ogb\u0026atic=1\u0026mo=1\u0026mn=1\u0026hl=en\u0026ts=250",0,"dashboard",null,null,null,null,"Profile","",1,null,"Signed out","https://accounts.google.com/AccountChooser?source=ogb\u0026continue=$continue\u0026Email=$email\u0026ec=GAhAqQM","https://accounts.google.com/RemoveLocalAccount?source=ogb","Remove","Sign in",0,1,1,0,1,1,0,null,null,null,"Session expired",null,null,null,"Visitor",null,"Default","Delegated","Sign out of all accounts",0,null,null,0,null,null,"myaccount.google.com","https",0,1,0],null,["1","gci_91f30755d6a6b787dcc2a4062e6e9824.js","googleapis.client:gapi.iframes","0","en"],null,null,null,null,["m;/_/scs/abc-static/_/js/k=gapi.gapi.en.iZZZ0XsR8bM.O/am=AAAQ/d=1/rs=AHpOoo_0-97nH_2IxP0suYF105-PdJv4zg/m=__features__","https://apis.google.com","","","1","",null,1,"es_plusone_gc_20240606.0_p0","en",null,0],[0.009999999776482582,"co.in","425",[null,"","0",null,1,5184000,null,null,"",null,null,null,null,null,0,null,0,null,1,0,0,0,null,null,0,0,null,0,0,0,0,0],null,null,null,0,null,null,["5061451","google\\.(com|ru|ca|by|kz|com\\.mx|com\\.tr)$",1]],[1,1,null,40400,425,"IND","en","648210890.0",8,1,1,0,null,null,null,null,"3700949,3701387,3701439,3701461",null,null,null,"xZqLZvvIMJ67wN4PqYimmA4",0,0,0,null,2,5,"nn",70,0,0,1,1,1,114591953,0,0],[[null,null,null,"https://www.gstatic.com/og/_/js/k=og.qtm.en_US.k_rHrBjflTk.2019.O/rt=j/m=qabr,qgl,q_dnp,qcwid,qbd,qapid,qrcd,q_dg/exm=qaaw,qadd,qaid,qein,qhaw,qhba,qhbr,qhch,qhga,qhid,qhin/d=1/ed=1/rs=AA2YrTt1hnGqeS6CLgm_ywEWql2sJwW4iA"],[null,null,null,"https://www.gstatic.com/og/_/ss/k=og.qtm.nuHTXYWlLd0.L.W.O/m=qcwid/excm=qaaw,qadd,qaid,qein,qhaw,qhba,qhbr,qhch,qhga,qhid,qhin/d=1/ed=1/ct=zgms/rs=AA2YrTuab1saMfPg0iiAR9TwFTm87PY2ug"]],null,null,null,[[[null,null,[null,null,null,"https://ogs.google.com/u/0/widget/account?amb=1\u0026sea=1"],0,414,436,57,4,1,0,0,65,66,8000,"https://accounts.google.com/SignOutOptions?hl=en\u0026continue=https://colab.research.google.com/drive/1UQ9tc9AaVNd7WtJUnMArlHDBSayfozb8\u0026ec=GBRAqQM",68,2,null,null,1,113,"Something went wrong.%1$s Refresh to try again or %2$schoose another account%3$s.",3,null,null,75,0,null,null,null,null,null,null,null,"/widget/account",["https","myaccount.google.com",0,32,83,0],0,0,1,["Critical security alert","Important account alert","Storage usage alert"],0,1,null,1,1,0,0,null,null,0,0,0,0,0,0]],null,null,"425","425",1,0,null,"en",0,["https://colab.research.google.com/drive/1UQ9tc9AaVNd7WtJUnMArlHDBSayfozb8?authuser=$authuser","https://accounts.google.com/AddSession?hl=en\u0026continue=https://colab.research.google.com/drive/1UQ9tc9AaVNd7WtJUnMArlHDBSayfozb8\u0026ec=GAlAqQM","https://accounts.google.com/Logout?hl=en\u0026continue=https://colab.research.google.com/drive/1UQ9tc9AaVNd7WtJUnMArlHDBSayfozb8\u0026timeStmp=1720425157\u0026secTok=.AG5fkS9DXtN4Nb0IPlV-t2z9Rqf52Tq84Q\u0026ec=GAdAqQM","https://accounts.google.com/ListAccounts?listPages=0\u0026pid=425\u0026gpsia=1\u0026source=ogb\u0026atic=1\u0026mo=1\u0026mn=1\u0026hl=en\u0026ts=250",0,0,"",0,0,null,0,0,"https://accounts.google.com/ServiceLogin?passive=true\u0026continue=https%3A%2F%2Fcolab.research.google.com%2Fdrive%2F1UQ9tc9AaVNd7WtJUnMArlHDBSayfozb8\u0026ec=GAZAqQM",0,0,0],0,0,0,null,0],null,[["mousedown","touchstart","touchmove","wheel","keydown"],300000],[[null,null,null,"https://accounts.google.com/RotateCookiesPage"],3,null,null,null,0,0]]],};this.gbar_=this.gbar_||{};(function(_){var window=this;
try{
_._F_toggles_initialize=function(a){(typeof globalThis!=="undefined"?globalThis:typeof self!=="undefined"?self:this)._F_toggles=a||[]};(0,_._F_toggles_initialize)([]);
/*

 Copyright The Closure Library Authors.
 SPDX-License-Identifier: Apache-2.0
*/
var fa,ha,la,na,oa,xa,ya,Aa,Ca,Da,Ea,Ha,Xa,Wa,Za,ab,$a,bb,cb,fb,gb,kb,nb,hb,mb,lb,jb,ib,ob,pb,zb,Bb,Cb,Db,Eb;_.aa=function(a,b){if(Error.captureStackTrace)Error.captureStackTrace(this,_.aa);else{const c=Error().stack;c&&(this.stack=c)}a&&(this.message=String(a));b!==void 0&&(this.cause=b)};_.ba=function(a){_.t.setTimeout(()=>{throw a;},0)};_.ca=function(){var a=_.t.navigator;return a&&(a=a.userAgent)?a:""};fa=function(a){return da?ea?ea.brands.some(({brand:b})=>b&&b.indexOf(a)!=-1):!1:!1};
_.u=function(a){return _.ca().indexOf(a)!=-1};ha=function(){return da?!!ea&&ea.brands.length>0:!1};_.ia=function(){return ha()?!1:_.u("Opera")};_.ja=function(){return ha()?!1:_.u("Trident")||_.u("MSIE")};_.ka=function(){return _.u("Firefox")||_.u("FxiOS")};_.ma=function(){return _.u("Safari")&&!(la()||(ha()?0:_.u("Coast"))||_.ia()||(ha()?0:_.u("Edge"))||(ha()?fa("Microsoft Edge"):_.u("Edg/"))||(ha()?fa("Opera"):_.u("OPR"))||_.ka()||_.u("Silk")||_.u("Android"))};
la=function(){return ha()?fa("Chromium"):(_.u("Chrome")||_.u("CriOS"))&&!(ha()?0:_.u("Edge"))||_.u("Silk")};na=function(){return da?!!ea&&!!ea.platform:!1};oa=function(){return _.u("iPhone")&&!_.u("iPod")&&!_.u("iPad")};_.pa=function(){return oa()||_.u("iPad")||_.u("iPod")};_.qa=function(){return na()?ea.platform==="macOS":_.u("Macintosh")};_.sa=function(a,b){return _.ra(a,b)>=0};
_.ta=function(a){let b="",c=0;const d=a.length-10240;for(;c<d;)b+=String.fromCharCode.apply(null,a.subarray(c,c+=10240));b+=String.fromCharCode.apply(null,c?a.subarray(c):a);return btoa(b)};_.ua=function(a){return a!=null&&a instanceof Uint8Array};_.va=function(a){return Array.prototype.slice.call(a)};xa=function(a,b){_.wa(b,(a|0)&-14591)};ya=function(a,b){_.wa(b,(a|34)&-14557)};Aa=function(a){a=a>>14&1023;return a===0?536870912:a};Ca=function(a){return!(!a||typeof a!=="object"||a.i!==Ba)};
Da=function(a){return a!==null&&typeof a==="object"&&!Array.isArray(a)&&a.constructor===Object};Ea=function(a,b,c){if(!Array.isArray(a)||a.length)return!1;const d=a[_.v]|0;if(d&1)return!0;if(!(b&&(Array.isArray(b)?b.includes(c):b.has(c))))return!1;_.wa(a,d|1);return!0};_.Fa=function(a){if(a&2)throw Error();};Ha=function(a,b){(b=_.Ga?b[_.Ga]:void 0)&&(a[_.Ga]=_.va(b))};_.Ja=function(){const a=Error();Ia(a,"incident");_.ba(a)};_.Ka=function(a){a=Error(a);Ia(a,"warning");return a};
_.Ma=function(a){if(typeof a!=="boolean")throw Error("s`"+_.La(a)+"`"+a);return a};_.Na=function(a){if(!Number.isFinite(a))throw _.Ka("enum");return a|0};_.Oa=function(a){if(typeof a!=="number")throw _.Ka("int32");if(!Number.isFinite(a))throw _.Ka("int32");return a|0};_.Pa=function(a){if(a!=null&&typeof a!=="string")throw Error();return a};_.Qa=function(a){return a==null||typeof a==="string"?a:void 0};
_.Sa=function(a,b,c){if(a!=null&&typeof a==="object"&&a.Gd===_.Ra)return a;if(Array.isArray(a)){var d=a[_.v]|0,e=d;e===0&&(e|=c&32);e|=c&2;e!==d&&_.wa(a,e);return new b(a)}};_.Ua=function(a,b){Ta=b;a=new a(b);Ta=void 0;return a};
_.Va=function(a,b,c){a==null&&(a=Ta);Ta=void 0;if(a==null){var d=96;c?(a=[c],d|=512):a=[];b&&(d=d&-16760833|(b&1023)<<14)}else{if(!Array.isArray(a))throw Error("t");d=a[_.v]|0;if(d&2048)throw Error("u");if(d&64)return a;d|=64;if(c&&(d|=512,c!==a[0]))throw Error("v");a:{c=a;const e=c.length;if(e){const f=e-1;if(Da(c[f])){d|=256;b=f-(+!!(d&512)-1);if(b>=1024)throw Error("w");d=d&-16760833|(b&1023)<<14;break a}}if(b){b=Math.max(b,e-(+!!(d&512)-1));if(b>1024)throw Error("x");d=d&-16760833|(b&1023)<<14}}}_.wa(a,
d);return a};Xa=function(a,b){return Wa(b)};Wa=function(a){switch(typeof a){case "number":return isFinite(a)?a:String(a);case "boolean":return a?1:0;case "object":if(a)if(Array.isArray(a)){if(Ea(a,void 0,0))return}else{if(_.ua(a))return _.ta(a);if("function"==typeof _.Ya&&a instanceof _.Ya)return a.j()}}return a};Za=function(a,b,c){const d=_.va(a);var e=d.length;const f=b&256?d[e-1]:void 0;e+=f?-1:0;for(b=b&512?1:0;b<e;b++)d[b]=c(d[b]);if(f){b=d[b]={};for(const g in f)b[g]=c(f[g])}Ha(d,a);return d};
ab=function(a,b,c,d,e){if(a!=null){if(Array.isArray(a))a=Ea(a,void 0,0)?void 0:e&&(a[_.v]|0)&2?a:$a(a,b,c,d!==void 0,e);else if(Da(a)){const f={};for(let g in a)f[g]=ab(a[g],b,c,d,e);a=f}else a=b(a,d);return a}};$a=function(a,b,c,d,e){const f=d||c?a[_.v]|0:0;d=d?!!(f&32):void 0;const g=_.va(a);for(let h=0;h<g.length;h++)g[h]=ab(g[h],b,c,d,e);c&&(Ha(g,a),c(f,g));return g};bb=function(a){return a.Gd===_.Ra?a.toJSON():Wa(a)};
cb=function(a,b,c=ya){if(a!=null){if(a instanceof Uint8Array)return b?a:new Uint8Array(a);if(Array.isArray(a)){var d=a[_.v]|0;d&2||(b&&(b=d===0||!!(d&32)&&!(d&64||!(d&16))),a=b?_.wa(a,(d|34)&-12293):$a(a,cb,d&4?ya:c,!0,!0));return a}a.Gd===_.Ra&&(c=a.na,d=c[_.v],a=d&2?a:_.Ua(a.constructor,_.db(c,d,!0)));return a}};_.db=function(a,b,c){const d=c||b&2?ya:xa,e=!!(b&32);a=Za(a,b,f=>cb(f,e,d));a[_.v]=a[_.v]|32|(c?2:0);return a};
_.eb=function(a){const b=a.na,c=b[_.v];return c&2?_.Ua(a.constructor,_.db(b,c,!1)):a};fb=function(a){return a};gb=function(a){return a};kb=function(a,b,c,d){return hb(a,b,c,d,ib,jb)};nb=function(a,b,c,d){return hb(a,b,c,d,lb,mb)};
hb=function(a,b,c,d,e,f){if(!c.length&&!d)return 0;var g=0;let h=0,k=0;var l=0;let m=0;for(var p=c.length-1;p>=0;p--){var r=c[p];d&&p===c.length-1&&r===d||(l++,r!=null&&k++)}if(d)for(var q in d)p=+q,isNaN(p)||(m+=ob(p),h++,p>g&&(g=p));l=e(l,k)+f(h,g,m);q=k;p=h;r=g;let y=m;for(let C=c.length-1;C>=0;C--){var G=c[C];if(G==null||d&&C===c.length-1&&G===d)continue;G=C-b;const E=e(G,q)+f(p,r,y);E<l&&(a=1+G,l=E);p++;q--;y+=ob(G);r=Math.max(r,G)}b=e(0,0)+f(p,r,y);b<l&&(a=0,l=b);if(d){p=h;r=g;y=m;q=k;for(const C in d)d=
+C,isNaN(d)||d>=1024||(p--,q++,y-=C.length,g=e(d,q)+f(p,r,y),g<l&&(a=1+d,l=g))}return a};mb=function(a,b,c){return c+a*3+(a>1?a-1:0)};lb=function(a,b){return(a>1?a-1:0)+(a-b)*4};jb=function(a,b){return a==0?0:9*Math.max(1<<32-Math.clz32(a+a/2-1),4)<=b?a==0?0:a<4?100+(a-1)*16:a<6?148+(a-4)*16:a<12?244+(a-6)*16:a<22?436+(a-12)*19:a<44?820+(a-22)*17:52+32*a:40+4*b};ib=function(a){return 40+4*a};ob=function(a){return a>=100?a>=1E4?Math.ceil(Math.log10(1+a)):a<1E3?3:4:a<10?1:2};
pb=function(a,b,c,d){b=d+(+!!(b&512)-1);if(!(b<0||b>=a.length||b>=c))return a[b]};_.rb=function(a,b,c,d,e){const f=Aa(b);if(c>=f||e&&!qb){let g=b;if(b&256)e=a[a.length-1];else{if(d==null)return g;e=a[f+(+!!(b&512)-1)]={};g|=256}e[c]=d;c<f&&(a[c+(+!!(b&512)-1)]=void 0);g!==b&&_.wa(a,g);return g}a[c+(+!!(b&512)-1)]=d;b&256&&(a=a[a.length-1],c in a&&delete a[c]);return b};_.tb=function(a,b,c,d){a=a.na;let e=a[_.v];const f=_.sb(a,e,c,d);b=_.Sa(f,b,e);b!==f&&b!=null&&_.rb(a,e,c,b,d);return b};
_.ub=function(a,b){return a!=null?a:b};
zb=function(a){var b=vb?a.na:$a(a.na,bb,void 0,void 0,!1);{var c=!vb;var d=wb?void 0:a.constructor.oa;var e=(c?a.na:b)[_.v];let A=b.length;if(A){var f=b[A-1],g=Da(f);g?A--:f=void 0;a=+!!(e&512)-1;var h=A-a,k=!!yb&&qb&&!(e&512),l;e=(l=yb)!=null?l:gb;e=k?e(h,a,b,f):h;l=(h=k&&h!==e)?Array.prototype.slice.call(b,0,A):b;if(g||h){b:{var m=l;var p=f;g={};k=!1;if(h)for(var r=Math.max(0,e+a);r<m.length;r++){var q=m[r],y=r-a;q==null||Ea(q,d,y)||Ca(q)&&q.size===0||(m[r]=void 0,g[y]=q,k=!0)}if(p)for(var G in p)if(r=
+G,isNaN(r))g[G]=p[G];else if(q=p[G],Array.isArray(q)&&(Ea(q,d,+G)||Ca(q)&&q.size===0)&&(q=null),q==null&&(k=!0),h&&r<e){k=!0;q=r+a;for(y=m.length;y<=q;y++)m.push(void 0);m[q]=p[r]}else q!=null&&(g[G]=q);if(k){for(var C in g){p=g;break b}p=null}}m=p==null?f!=null:p!==f}h&&(A=l.length);for(var E;A>0;A--){C=A-1;G=l[C];C-=a;if(!(G==null||Ea(G,d,C)||Ca(G)&&G.size===0))break;E=!0}if(l!==b||m||E){if(!h&&!c)l=Array.prototype.slice.call(l,0,A);else if(E||m||p)l.length=A;p&&l.push(p)}b=l}}return b};
_.w=function(a,b){return a!=null?!!a:!!b};_.x=function(a,b){b==void 0&&(b="");return a!=null?a:b};_.Ab=function(a){for(const b in a)return!1;return!0};Bb=typeof Object.defineProperties=="function"?Object.defineProperty:function(a,b,c){if(a==Array.prototype||a==Object.prototype)return a;a[b]=c.value;return a};
Cb=function(a){a=["object"==typeof globalThis&&globalThis,a,"object"==typeof window&&window,"object"==typeof self&&self,"object"==typeof global&&global];for(var b=0;b<a.length;++b){var c=a[b];if(c&&c.Math==Math)return c}throw Error("a");};Db=Cb(this);Eb=function(a,b){if(b)a:{var c=Db;a=a.split(".");for(var d=0;d<a.length-1;d++){var e=a[d];if(!(e in c))break a;c=c[e]}a=a[a.length-1];d=c[a];b=b(d);b!=d&&b!=null&&Bb(c,a,{configurable:!0,writable:!0,value:b})}};
Eb("Symbol.dispose",function(a){return a?a:Symbol("b")});Eb("globalThis",function(a){return a||Db});Eb("Promise.prototype.finally",function(a){return a?a:function(b){return this.then(function(c){return Promise.resolve(b()).then(function(){return c})},function(c){return Promise.resolve(b()).then(function(){throw c;})})}});var Hb,Ib,Kb,Lb;_.Fb=_.Fb||{};_.t=this||self;Hb=function(a,b){var c=_.Gb("WIZ_global_data.oxN3nb");a=c&&c[a];return a!=null?a:b};Ib=_.t._F_toggles||[];_.Gb=function(a,b){a=a.split(".");b=b||_.t;for(var c=0;c<a.length;c++)if(b=b[a[c]],b==null)return null;return b};_.La=function(a){var b=typeof a;return b!="object"?b:a?Array.isArray(a)?"array":b:"null"};_.Jb="closure_uid_"+(Math.random()*1E9>>>0);Kb=function(a,b,c){return a.call.apply(a.bind,arguments)};
Lb=function(a,b,c){if(!a)throw Error();if(arguments.length>2){var d=Array.prototype.slice.call(arguments,2);return function(){var e=Array.prototype.slice.call(arguments);Array.prototype.unshift.apply(e,d);return a.apply(b,e)}}return function(){return a.apply(b,arguments)}};_.z=function(a,b,c){_.z=Function.prototype.bind&&Function.prototype.bind.toString().indexOf("native code")!=-1?Kb:Lb;return _.z.apply(null,arguments)};
_.B=function(a,b){a=a.split(".");var c=_.t;a[0]in c||typeof c.execScript=="undefined"||c.execScript("var "+a[0]);for(var d;a.length&&(d=a.shift());)a.length||b===void 0?c[d]&&c[d]!==Object.prototype[d]?c=c[d]:c=c[d]={}:c[d]=b};_.D=function(a,b){function c(){}c.prototype=b.prototype;a.W=b.prototype;a.prototype=new c;a.prototype.constructor=a;a.fj=function(d,e,f){for(var g=Array(arguments.length-2),h=2;h<arguments.length;h++)g[h-2]=arguments[h];return b.prototype[e].apply(d,g)}};_.D(_.aa,Error);_.aa.prototype.name="CustomError";var Mb=!!(Ib[0]&1024),Nb=!!(Ib[0]&32),Ob=!!(Ib[0]&2048),Pb=!!(Ib[0]&16),Qb=!!(Ib[0]&8);var Rb=Hb(1,!0),da=Mb?Ob:Hb(610401301,!1),qb=Mb?Nb||!Qb:Hb(645172343,Rb);var wb=Mb?Nb||!Pb:Hb(188588736,Rb);_.Sb=typeof TextDecoder!=="undefined";_.Tb=typeof TextEncoder!=="undefined";_.Ub=String.prototype.trim?function(a){return a.trim()}:function(a){return/^[\s\xa0]*([\s\S]*?)[\s\xa0]*$/.exec(a)[1]};var ea,Vb=_.t.navigator;ea=Vb?Vb.userAgentData||null:null;_.ra=function(a,b){return Array.prototype.indexOf.call(a,b,void 0)};_.Wb=function(a,b,c){Array.prototype.forEach.call(a,b,c)};_.Xb=function(a){_.Xb[" "](a);return a};_.Xb[" "]=function(){};var jc;_.Yb=_.ia();_.Zb=_.ja();_.$b=_.u("Edge");_.ac=_.u("Gecko")&&!(_.ca().toLowerCase().indexOf("webkit")!=-1&&!_.u("Edge"))&&!(_.u("Trident")||_.u("MSIE"))&&!_.u("Edge");_.bc=_.ca().toLowerCase().indexOf("webkit")!=-1&&!_.u("Edge");_.cc=_.qa();_.dc=na()?ea.platform==="Windows":_.u("Windows");_.ec=na()?ea.platform==="Android":_.u("Android");_.fc=oa();_.gc=_.u("iPad");_.hc=_.u("iPod");_.ic=_.pa();
a:{var kc="",lc=function(){var a=_.ca();if(_.ac)return/rv:([^\);]+)(\)|;)/.exec(a);if(_.$b)return/Edge\/([\d\.]+)/.exec(a);if(_.Zb)return/\b(?:MSIE|rv)[: ]([^\);]+)(\)|;)/.exec(a);if(_.bc)return/WebKit\/(\S+)/.exec(a);if(_.Yb)return/(?:Version)[ \/]?(\S+)/.exec(a)}();lc&&(kc=lc?lc[1]:"");if(_.Zb){var mc,nc=_.t.document;mc=nc?nc.documentMode:void 0;if(mc!=null&&mc>parseFloat(kc)){jc=String(mc);break a}}jc=kc}_.oc=jc;_.pc=_.ka();_.qc=oa()||_.u("iPod");_.rc=_.u("iPad");_.sc=_.u("Android")&&!(la()||_.ka()||_.ia()||_.u("Silk"));_.tc=la();_.uc=_.ma()&&!_.pa();var vc;_.v=Symbol();vc=Symbol();_.wc=Symbol();_.xc=Symbol();_.wa=(a,b)=>{a[_.v]=b;return a};var Ba,zc;_.Ra={};Ba={};zc=[];_.wa(zc,55);_.yc=Object.freeze(zc);Object.freeze({});Object.freeze({});_.Ac=Object.freeze({});var Ia=function(a,b){a.__closure__error__context__984382||(a.__closure__error__context__984382={});a.__closure__error__context__984382.severity=b};var Bc;var Ta;_.Cc=function(a,b){a=a.na;return _.sb(a,a[_.v],b)};_.sb=function(a,b,c,d){if(c===-1)return null;const e=Aa(b);if(c>=e){if(b&256)return a[a.length-1][c]}else{var f=a.length;if(d&&b&256&&(d=a[f-1][c],d!=null)){if(pb(a,b,e,c)&&vc!=null){var g;a=(g=Bc)!=null?g:Bc={};g=a[vc]||0;g>=4||(a[vc]=g+1,_.Ja())}return d}return pb(a,b,e,c)}};_.Dc=function(a,b,c){const d=a.na;let e=d[_.v];_.Fa(e);_.rb(d,e,b,c);return a};
_.F=function(a,b,c,d=!1){b=_.tb(a,b,c,d);if(b==null)return b;a=a.na;let e=a[_.v];if(!(e&2)){const f=_.eb(b);f!==b&&(b=f,_.rb(a,e,c,b,d))}return b};_.H=function(a,b,c){c==null&&(c=void 0);return _.Dc(a,b,c)};_.I=function(a,b){a=_.Cc(a,b);return a==null||typeof a==="boolean"?a:typeof a==="number"?!!a:void 0};_.J=function(a,b){return _.Qa(_.Cc(a,b))};_.K=function(a,b,c=!1){return _.ub(_.I(a,b),c)};_.L=function(a,b){return _.ub(_.J(a,b),"")};_.M=function(a,b,c){return _.Dc(a,b,c==null?c:_.Ma(c))};
_.N=function(a,b,c){return _.Dc(a,b,c==null?c:_.Oa(c))};_.O=function(a,b,c){return _.Dc(a,b,_.Pa(c))};_.P=function(a,b,c){return _.Dc(a,b,c==null?c:_.Na(c))};var yb,vb;_.Q=class{constructor(a,b,c){this.na=_.Va(a,b,c)}toJSON(){return zb(this)}Fa(a){try{return vb=!0,a&&(yb=a===gb||a!==fb&&a!==kb&&a!==nb?gb:a),JSON.stringify(zb(this),Xa)}finally{a&&(yb=void 0),vb=!1}}vc(){return!!((this.na[_.v]|0)&2)}};_.Q.prototype.Gd=_.Ra;_.Q.prototype.toString=function(){try{return vb=!0,zb(this).toString()}finally{vb=!1}};_.Ec=Symbol();_.Fc=Symbol();_.Gc=Symbol();_.Hc=Symbol();_.Ic=Symbol();var Jc=class extends _.Q{constructor(){super()}};_.Kc=class extends _.Q{constructor(){super()}D(a){return _.N(this,3,a)}};_.Kc.oa=[67];var Lc=class extends _.Q{constructor(a){super(a)}Mc(a){return _.O(this,24,a)}};_.Mc=class extends _.Q{constructor(a){super(a)}};_.R=function(){this.Da=this.Da;this.ea=this.ea};_.R.prototype.Da=!1;_.R.prototype.isDisposed=function(){return this.Da};_.R.prototype.dispose=function(){this.Da||(this.Da=!0,this.P())};_.R.prototype.P=function(){if(this.ea)for(;this.ea.length;)this.ea.shift()()};var Nc=class extends _.R{constructor(){var a=window;super();this.o=a;this.i=[];this.j={}}resolve(a){var b=this.o;a=a.split(".");for(var c=a.length,d=0;d<c;++d)if(b[a[d]])b=b[a[d]];else return null;return b instanceof Function?b:null}Cb(){for(var a=this.i.length,b=this.i,c=[],d=0;d<a;++d){var e=b[d].i(),f=this.resolve(e);if(f&&f!=this.j[e])try{b[d].Cb(f)}catch(g){}else c.push(b[d])}this.i=c.concat(b.slice(a))}};var Pc=class extends _.R{constructor(){var a=_.Oc;super();this.o=a;this.A=this.i=null;this.v=0;this.B={};this.j=!1;a=window.navigator.userAgent;a.indexOf("MSIE")>=0&&a.indexOf("Trident")>=0&&(a=/\b(?:MSIE|rv)[: ]([^\);]+)(\)|;)/.exec(a))&&a[1]&&parseFloat(a[1])<9&&(this.j=!0)}C(a,b){this.i=b;this.A=a;b.preventDefault?b.preventDefault():b.returnValue=!1}};_.Qc=class extends _.Q{constructor(a){super(a)}};var Rc=class extends _.Q{constructor(a){super(a)}};var Uc;_.Sc=function(a,b,c=98,d=new _.Kc){if(a.i){const e=new Jc;_.O(e,1,b.message);_.O(e,2,b.stack);_.N(e,3,b.lineNumber);_.P(e,5,1);_.H(d,40,e);a.i.log(c,d)}};Uc=class{constructor(){var a=Tc;this.i=null;_.K(a,4,!0)}log(a,b,c=new _.Kc){_.Sc(this,a,98,c)}};var Vc,Wc;Vc=function(a){if(a.o.length>0){var b=a.i!==void 0,c=a.j!==void 0;if(b||c){b=b?a.v:a.A;c=a.o;a.o=[];try{_.Wb(c,b,a)}catch(d){console.error(d)}}}};_.Xc=class{constructor(a){this.i=a;this.j=void 0;this.o=[]}then(a,b,c){this.o.push(new Wc(a,b,c));Vc(this)}resolve(a){if(this.i!==void 0||this.j!==void 0)throw Error("C");this.i=a;Vc(this)}reject(a){if(this.i!==void 0||this.j!==void 0)throw Error("C");this.j=a;Vc(this)}v(a){a.j&&a.j.call(a.i,this.i)}A(a){a.o&&a.o.call(a.i,this.j)}};
Wc=class{constructor(a,b,c){this.j=a;this.o=b;this.i=c}};_.Yc=a=>{var b="tc";if(a.tc&&a.hasOwnProperty(b))return a.tc;b=new a;return a.tc=b};_.Zc=class{constructor(){this.v=new _.Xc;this.i=new _.Xc;this.D=new _.Xc;this.B=new _.Xc;this.C=new _.Xc;this.A=new _.Xc;this.o=new _.Xc;this.j=new _.Xc;this.F=new _.Xc}K(){return this.v}M(){return this.i}N(){return this.D}L(){return this.B}Da(){return this.C}ea(){return this.A}J(){return this.o}G(){return this.j}static i(){return _.Yc(_.Zc)}};var dd;_.ad=function(){return _.F(_.$c,Lc,1)};_.bd=function(){return _.F(_.$c,_.Mc,5)};dd=class extends _.Q{constructor(){super(cd)}};var cd;window.gbar_&&window.gbar_.CONFIG?cd=window.gbar_.CONFIG[0]||{}:cd=[];_.$c=new dd;var Tc=_.F(_.$c,Rc,3)||new Rc;_.ad()||new Lc;_.Oc=new Uc;_.B("gbar_._DumpException",function(a){_.Oc?_.Oc.log(a):console.error(a)});_.ed=new Pc;var gd;_.hd=function(a,b){var c=_.fd.i();if(a in c.i){if(c.i[a]!=b)throw new gd;}else{c.i[a]=b;const h=c.j[a];if(h)for(let k=0,l=h.length;k<l;k++){b=h[k];var d=c.i;delete b.i[a];if(_.Ab(b.i)){for(var e=b.j.length,f=Array(e),g=0;g<e;g++)f[g]=d[b.j[g]];b.o.apply(b.v,f)}}delete c.j[a]}};_.fd=class{constructor(){this.i={};this.j={}}static i(){return _.Yc(_.fd)}};_.id=class extends _.aa{constructor(){super()}};gd=class extends _.id{};_.B("gbar.A",_.Xc);_.Xc.prototype.aa=_.Xc.prototype.then;_.B("gbar.B",_.Zc);_.Zc.prototype.ba=_.Zc.prototype.M;_.Zc.prototype.bb=_.Zc.prototype.N;_.Zc.prototype.bd=_.Zc.prototype.Da;_.Zc.prototype.bf=_.Zc.prototype.K;_.Zc.prototype.bg=_.Zc.prototype.L;_.Zc.prototype.bh=_.Zc.prototype.ea;_.Zc.prototype.bj=_.Zc.prototype.J;_.Zc.prototype.bk=_.Zc.prototype.G;_.B("gbar.a",_.Zc.i());window.gbar&&window.gbar.ap&&window.gbar.ap(window.gbar.a);var jd=new Nc;_.hd("api",jd);
var kd=_.bd()||new _.Mc,ld=window,md=_.x(_.J(kd,8));ld.__PVT=md;_.hd("eq",_.ed);
}catch(e){_._DumpException(e)}
try{
_.nd=class extends _.Q{constructor(a){super(a)}};
}catch(e){_._DumpException(e)}
try{
var od=class extends _.Q{constructor(){super()}};var pd=class extends _.R{constructor(){super();this.j=[];this.i=[]}o(a,b){this.j.push({features:a,options:b})}init(a,b,c){window.gapi={};var d=window.___jsl={};d.h=_.x(_.J(a,1));_.I(a,12)!=null&&(d.dpo=_.w(_.K(a,12)));d.ms=_.x(_.J(a,2));d.m=_.x(_.J(a,3));d.l=[];_.L(b,1)&&(a=_.J(b,3))&&this.i.push(a);_.L(c,1)&&(c=_.J(c,2))&&this.i.push(c);_.B("gapi.load",(0,_.z)(this.o,this));return this}};var qd=_.F(_.$c,_.Qc,14);if(qd){var rd=_.F(_.$c,_.nd,9)||new _.nd,sd=new od,td=new pd;td.init(qd,rd,sd);_.hd("gs",td)};
}catch(e){_._DumpException(e)}
})(this.gbar_);
// Google Inc.
</script><script nonce="">try {const preferences = JSON.parse(window.localStorage.getItem("datalab_prefs_indlanithish2002@gmail.com")); document.querySelector('html') .setAttribute('theme', preferences['siteTheme'] || 'default');} catch (e) {}</script><script nonce="">window.performance.mark('head_start');</script><link rel="stylesheet" href="./Task 1 - Chatbot with Rule-based responses_files/bundle.css"><script nonce="">var colabVersionTag = 'colab_20240703-060140_RC00_649031487'; var colabScsVersion = 'b975a0c32eb2cd1821902aeadd1622b8'; var hl = 'en'; var colabExperiments = JSON.parse('\x7b\x22ai_unsubscribed_warning\x22: true, \x22aida_complete_code_model_id\x22: \x22\x22, \x22aida_do_conversation_model_id\x22: \x22\x22, \x22aida_generate_code_model_id\x22: \x22\x22, \x22aida_in_editor\x22: false, \x22allowed_public_url_domains\x22: \x5b\x22huggingface.co\x22, \x22dagshub.com\x22, \x22storage.googleapis.com\x22\x5d, \x22auto_execute_prereqs\x22: false, \x22backend_version\x22: \x22next\x22, \x22cell_tags\x22: false, \x22chat\x22: true, \x22chat_model_id_override\x22: \x22\x22, \x22classified_generate\x22: false, \x22classroom_iframe_parent_origin\x22: \x22\x22, \x22client_text_compose\x22: true, \x22client_trim_completion_text\x22: 400, \x22cloud_origin\x22: \x22\x22, \x22commands_in_toolbar\x22: false, \x22comment_poll_long\x22: 900000, \x22comment_poll_short\x22: 60000, \x22compose_skip_suffix_check\x22: false, \x22converse_server_side_history\x22: false, \x22converse_temp\x22: \x22\x22, \x22crawler\x22: false, \x22critique_comments\x22: false, \x22dbu\x22: \x22\x22, \x22debug_external\x22: \x22external\x22, \x22debug_prod\x22: \x22prod\x22, \x22dep_cells_commands\x22: false, \x22dep_graph\x22: false, \x22development\x22: false, \x22document_change_poll_interval\x22: 30000, \x22drive_anon_api_key\x22: \x22AIzaSyB10s2vWUTwP0pj20wZoxmpZIt3rRodYeg\x22, \x22drive_api_key\x22: \x22AIzaSyCN_sSPJMpYrAzC5AtTrltNC8oRmLtoqBk\x22, \x22drive_background_save_project_number\x22: \x22948411933973\x22, \x22drive_realtime_project_number\x22: \x22\x22, \x22embedded_connection_poll\x22: false, \x22embedded_one_pending_connect_request\x22: false, \x22embedding_app\x22: \x22\x22, \x22enable_adhoc_backends\x22: false, \x22enable_dasher_subscription_ui\x22: false, \x22enable_more_reprs\x22: true, \x22explain_cell\x22: false, \x22explain_error\x22: true, \x22explain_error_model_id_override\x22: \x22\x22, \x22explain_error_prompt_next\x22: true, \x22explain_error_trim_traceback\x22: true, \x22explicit_ai_backend\x22: \x22\x22, \x22external_trusted_github_org_repos_quick_add\x22: \x22GoogleChrome\/CrUX,google\/generative-ai-docs\x22, \x22file_upload_rate_limit\x22: 5, \x22filter_repetitive_suggestions\x22: false, \x22first_party_auth\x22: true, \x22fix_imports\x22: false, \x22gemini_rebrand\x22: true, \x22generate_code\x22: true, \x22generate_df\x22: true, \x22generate_prompt_reduce_name_errors\x22: true, \x22generate_temp\x22: \x22\x22, \x22get_started\x22: false, \x22gis_auth\x22: true, \x22github_client_id\x22: \x225036cf6d81e65aaa6340\x22, \x22gpu_utilization_check_interval_ms\x22: 600000, \x22granular_browser_permissions\x22: false, \x22hats_surveys\x22: true, \x22hide_fix_error_for_long_code\x22: false, \x22hrc\x22: false, \x22import_data\x22: false, \x22interactive_sheet_next_steps\x22: false, \x22internal_chat\x22: false, \x22internal_schedule\x22: false, \x22is_prober\x22: false, \x22jsraw\x22: \x22compiled\x22, \x22key_promoter\x22: false, \x22kr\x22: false, \x22local_cloud_apis\x22: false, \x22local_service_worker\x22: false, \x22lsp_diagnostic_threshold_b312769838\x22: 0, \x22lsp_diagnostics_reporting\x22: false, \x22lsp_inlay_hint\x22: false, \x22lsrp\x22: 0, \x22ml_banner\x22: false, \x22ml_enabled\x22: true, \x22mlpp\x22: false, \x22mlpp_multiline\x22: false, \x22mlpp_on_by_default\x22: true, \x22mobile\x22: false, \x22next_steps\x22: true, \x22nl2code_missing_imports\x22: true, \x22no_fun\x22: false, \x22notebook_context_length\x22: 10000, \x22outage_notification\x22: \x22\x22, \x22outage_notification_link\x22: \x22\x22, \x22output_menu\x22: true, \x22outputframe_version\x22: \x22\x22, \x22override_suf_params_for_test\x22: false, \x22prereq_cells_next_steps\x22: false, \x22recaptcha_polling_frequency_ms\x22: 300000, \x22recaptcha_v2_site_key\x22: \x226LfQttQUAAAAADuPanA_VZMaZgBAOnHZNuuqUewp\x22, \x22recaptcha_v3_site_key\x22: \x226LfQPtEUAAAAAHBpAdFng54jyuB1V5w5dofknpip\x22, \x22reconnect_max_delay_seconds\x22: 300, \x22reduce_chat_not_answering\x22: false, \x22require_ai_consent\x22: true, \x22resource_poll_interval_ms\x22: 10000, \x22rp_kxhr\x22: false, \x22rp_lsp\x22: true, \x22rp_serve_kernel_port\x22: false, \x22rp_term\x22: true, \x22rp_token_refresh_headroom_millis\x22: 300000, \x22rt\x22: false, \x22runtime_env_overrides\x22: \x22\\n          \x5b\\n            \x5b\\\x22ENABLE_DIRECTORYPREFETCHER\\\x22, \\\x221\\\x22\x5d\\n          \x5d\\n        \x22, \x22runtime_type_for_test\x22: \x22\x22, \x22server_execution_queue\x22: true, \x22session_resume_coalesce\x22: true, \x22show_internal_ai_warning\x22: false, \x22show_payments_interstitial\x22: false, \x22show_relnotes_on_open\x22: true, \x22show_signup_survey\x22: true, \x22show_subscription_renewal_time\x22: false, \x22show_switch_to_prod_link\x22: false, \x22smartpaste\x22: false, \x22smartpaste_serving_config\x22: \x22pl_700m_smart_paste_3.0.25\x22, \x22sql_cell\x22: false, \x22sql_cell_buttons\x22: false, \x22storage_partition_trial\x22: true, \x22storage_partition_trial_token\x22: \x22AmUpB2+Hlwk73pYiEMbnkef\/dprJi1I9rClec33apyFsbVOaCIRN29Rk9M4ht5Otgbp+thCc3MMD73GyCNfEWAkAAAB3eyJvcmlnaW4iOiJodHRwczovL2NvbGFiLnJlc2VhcmNoLmdvb2dsZS5jb206NDQzIiwiZmVhdHVyZSI6IkRpc2FibGVUaGlyZFBhcnR5U3RvcmFnZVBhcnRpdGlvbmluZyIsImV4cGlyeSI6MTcyNTQwNzk5OX0\x3d\x22, \x22suspicious_code_matches\x22: \x22\x22, \x22suspicious_code_regexs\x22: \x22\x22, \x22term4all\x22: false, \x22text_compose_report_changes_millis\x22: 10000, \x22text_span_comments\x22: false, \x22tpu_node_deprecation_warning\x22: true, \x22tpu_node_redirect\x22: false, \x22tpu_node_selector_grayed_out\x22: true, \x22tpu_node_selector_visible\x22: true, \x22tpu_vm\x22: true, \x22unmanaged_vm_min_label_block\x22: \x22\x22, \x22unmanaged_vm_min_label_warn\x22: \x22\x22, \x22unmanaged_vm_min_release_tag_block\x22: \x22\x22, \x22unmanaged_vm_min_release_tag_warn\x22: \x22\x22, \x22use_corplogin\x22: true, \x22use_dm_sql_lsp\x22: false, \x22use_upticks_for_internalai\x22: false, \x22user_visible_gpu_types\x22: \x5b\x22T4\x22, \x22A100\x22, \x22L4\x22\x5d, \x22verbose_warnings\x22: false, \x22vertex_ai_api_environment_override\x22: \x22\x22, \x22waffle\x22: false, \x22workstations\x22: false, \x22ids\x22: \x5b20730177, 20730227, 20730258, 20730267, 20730129, 20730150, 20730250, 20730253, 20730185, 20730189, 20730183, 20730230, 20730224, 20730159\x5d, \x22flag_ids\x22: \x7b\x22ai_unsubscribed_warning\x22: 45504730, \x22aida_complete_code_model_id\x22: 45427660, \x22aida_do_conversation_model_id\x22: 45427664, \x22aida_generate_code_model_id\x22: 45427663, \x22aida_in_editor\x22: 45425507, \x22allowed_public_url_domains\x22: 45425558, \x22auto_execute_prereqs\x22: 45624305, \x22backend_version\x22: 45425541, \x22cell_tags\x22: 45425779, \x22chat\x22: 45425490, \x22chat_model_id_override\x22: 45631876, \x22classified_generate\x22: 45425499, \x22classroom_iframe_parent_origin\x22: 45425537, \x22client_text_compose\x22: 45425512, \x22client_trim_completion_text\x22: 45425628, \x22cloud_origin\x22: 45425538, \x22commands_in_toolbar\x22: 45425502, \x22comment_poll_long\x22: 45425588, \x22comment_poll_short\x22: 45425587, \x22compose_skip_suffix_check\x22: 45615470, \x22converse_server_side_history\x22: 45634472, \x22converse_temp\x22: 45425509, \x22crawler\x22: 45425491, \x22critique_comments\x22: 45612076, \x22dbu\x22: 45425545, \x22debug_external\x22: 45425470, \x22debug_prod\x22: 45425471, \x22dep_cells_commands\x22: 45622249, \x22dep_graph\x22: 45629071, \x22development\x22: 45425544, \x22document_change_poll_interval\x22: 45425589, \x22drive_anon_api_key\x22: 45425478, \x22drive_api_key\x22: 45425473, \x22drive_background_save_project_number\x22: 45425479, \x22drive_realtime_project_number\x22: 45425629, \x22embedded_connection_poll\x22: 45491618, \x22embedded_one_pending_connect_request\x22: 45640470, \x22enable_adhoc_backends\x22: 45425506, \x22enable_dasher_subscription_ui\x22: 45639531, \x22enable_more_reprs\x22: 45613354, \x22explain_cell\x22: 45425505, \x22explain_error\x22: 45425487, \x22explain_error_model_id_override\x22: 45631875, \x22explain_error_prompt_next\x22: 45615229, \x22explain_error_trim_traceback\x22: 45618831, \x22explicit_ai_backend\x22: 45638548, \x22external_trusted_github_org_repos_quick_add\x22: 45425555, \x22file_upload_rate_limit\x22: 45637799, \x22filter_repetitive_suggestions\x22: 45615781, \x22first_party_auth\x22: 45425560, \x22fix_imports\x22: 45624140, \x22gemini_rebrand\x22: 45631310, \x22generate_code\x22: 45425492, \x22generate_df\x22: 45425503, \x22generate_prompt_reduce_name_errors\x22: 45634392, \x22generate_temp\x22: 45425508, \x22get_started\x22: 45430267, \x22gis_auth\x22: 45425625, \x22github_client_id\x22: 45425556, \x22gpu_utilization_check_interval_ms\x22: 45425561, \x22granular_browser_permissions\x22: 45630936, \x22hats_surveys\x22: 45425559, \x22hide_fix_error_for_long_code\x22: 45638639, \x22import_data\x22: 45430411, \x22interactive_sheet_next_steps\x22: 45634324, \x22internal_chat\x22: 45622872, \x22internal_schedule\x22: 45425578, \x22is_prober\x22: 45429104, \x22jsraw\x22: 45425557, \x22key_promoter\x22: 45425570, \x22local_cloud_apis\x22: 45425630, \x22local_service_worker\x22: 45425550, \x22lsp_diagnostic_threshold_b312769838\x22: 45618432, \x22lsp_diagnostics_reporting\x22: 45425604, \x22lsp_inlay_hint\x22: 45614695, \x22lsrp\x22: 45425612, \x22ml_banner\x22: 45425631, \x22ml_enabled\x22: 45425493, \x22mlpp\x22: 45425608, \x22mlpp_multiline\x22: 45425623, \x22mlpp_on_by_default\x22: 45425609, \x22mobile\x22: 45425562, \x22next_steps\x22: 45428239, \x22nl2code_missing_imports\x22: 45615676, \x22no_fun\x22: 45425540, \x22notebook_context_length\x22: 45633457, \x22outage_notification\x22: 45425584, \x22outage_notification_link\x22: 45425585, \x22output_menu\x22: 45617054, \x22outputframe_version\x22: 45425591, \x22override_suf_params_for_test\x22: 45425592, \x22prereq_cells_next_steps\x22: 45640400, \x22recaptcha_polling_frequency_ms\x22: 45425582, \x22recaptcha_v2_site_key\x22: 45425581, \x22recaptcha_v3_site_key\x22: 45425580, \x22reconnect_max_delay_seconds\x22: 45425539, \x22reduce_chat_not_answering\x22: 45640977, \x22require_ai_consent\x22: 45425489, \x22resource_poll_interval_ms\x22: 45425590, \x22rp_kxhr\x22: 45491686, \x22rp_lsp\x22: 45462965, \x22rp_serve_kernel_port\x22: 45572083, \x22rp_term\x22: 45426219, \x22rp_token_refresh_headroom_millis\x22: 45517773, \x22rt\x22: 45425624, \x22runtime_env_overrides\x22: 45425583, \x22runtime_type_for_test\x22: 45425586, \x22server_execution_queue\x22: 45425600, \x22session_resume_coalesce\x22: 45425603, \x22show_internal_ai_warning\x22: 45622780, \x22show_payments_interstitial\x22: 45425543, \x22show_relnotes_on_open\x22: 45428128, \x22show_signup_survey\x22: 45425620, \x22show_subscription_renewal_time\x22: 45425569, \x22show_switch_to_prod_link\x22: 45425483, \x22smartpaste\x22: 45627425, \x22smartpaste_serving_config\x22: 45630585, \x22sql_cell\x22: 45425497, \x22sql_cell_buttons\x22: 45425498, \x22suspicious_code_matches\x22: 45425615, \x22suspicious_code_regexs\x22: 45425616, \x22term4all\x22: 45425542, \x22text_compose_report_changes_millis\x22: 45425568, \x22text_span_comments\x22: 45545873, \x22tpu_node_deprecation_warning\x22: 45630619, \x22tpu_node_redirect\x22: 45634372, \x22tpu_node_selector_grayed_out\x22: 45630664, \x22tpu_node_selector_visible\x22: 45630663, \x22tpu_vm\x22: 45614812, \x22unmanaged_vm_min_label_block\x22: 45425546, \x22unmanaged_vm_min_label_warn\x22: 45425547, \x22unmanaged_vm_min_release_tag_block\x22: 45425548, \x22unmanaged_vm_min_release_tag_warn\x22: 45425549, \x22use_corplogin\x22: 45425606, \x22use_dm_sql_lsp\x22: 45425610, \x22use_upticks_for_internalai\x22: 45629267, \x22user_visible_gpu_types\x22: 45620529, \x22verbose_warnings\x22: 45425551, \x22vertex_ai_api_environment_override\x22: 45612077, \x22waffle\x22: 45446491, \x22workstations\x22: 45425626\x7d\x7d'); var colabUserEmail = 'indlanithish2002@gmail.com'; var colabRenderDataToken = 'AFWLbD29LdUoh1rIgN5HqjI23aHlg8epRZ0awRiH6Is7Y0FJ8HTYqloIDpoHCQb33rUUcwdLbIi6GW-wMVT8IpaGpCTJ0tLR3C-r'; var colabConfig = '\x5b\x5b\x22indlanithish2002@gmail.com\x22,\x5b1,\x22AHXL0D3jRQnsGP9I57G91eGGIxiVcNWIi7JyaGGtPYEKhUIevYk3oX\/9fZvtEQhUob6nZywtjx3AsRatu0hC\/o5dgyVYQ9xZBLVu6WyI7BsFH+yYXQmWCAH6zDJB0JBXVeBQs6Ml6qErrVn\/OoVQE1qggaDfadyzw5dGl8y43501mo7LDiiwaB9eKI+CpaymDogLsKkle23sAiZRqT6zWPuTojWWCztinrYGSZ6dXblVIXAmhfxxBWoBqfWrLRPy8i2BQ0tWiZNK6ik4NsmXjH8qN2Nfs0yvhtnfWoLKWfYyVqOkYJXbb\/yHJTUar1fUegHPufkf\/x8TwA5joyIKCBPWD5Aq0\/vj8YmyFX7JdZfn0Q12LsVCSxocvrnMOn8e2Z8DkVg8UAka46RUhv2EV56kHgtn4yCcsPAtLUQLgGf1aMDZibxmze3p93xMFWRpJCazqbV8IeDS\/paY1U\/6TjMrQPLW9oRfsFGc0xumE\/o6uMcItZZxtcJkDTeV3A9WJCOngBXeAPm5dtMHpxJrlVSDvzSuj+LT6jrtmFRfQaBS8yE3rE++GH37nuJDI1xYYZlQ3j3gPMtgrghnEQS2GMJWy1h33pEdZc80oaCCXO\/wns2jsFZKwD97l0Vo15VRfOh00lMKWsnd25L\/yQmX8hM0\/1GOQHUh4BMSg4TVWO3y1SK8ePGnkhojVUK8GtqOUDJO05Dxs+3tt6tkPKRKMJq+QMpyqbiG4bE17khrwJWPgyxtLOIv8WOLyee8ahSqdiBtBMsXnML3TWuDRs3ZX\/IBBLDBB48i8kdZXJ3mQJ0WflH29Amni5Xuf4AHFjEcEGUdxA+t9LD4J+c4JufVWOKjFPV41y+A3+Tmxux6osuHCsAl1qG2NQlFUcZRnuPf8IjmqlLpOS5HGSD8S01g3EqvlGNebAhYlE26\/qKZcudRJk2zG3EbIMeb80J+tYj7FNOptfjpb3dzsAXRdGscPd6Lz4Es0JjhkdTYrkFNrpGD5kSd63RPhha+oXfJSDFacehxx4+AOFgAKLpoqyqY7lLqG67TwmqxTc0dFNQYO1YM4I0Is+lUURifP5tW\/ii52URsLOgBru\/wtPJ9VmaL4O7XjlnEye9hFsCA5w9fJKsL4z4fepCU1soYvy0Ytw8IrkDlg92NmQBl1Rt2ErWaKEb\/OgECQp++RkJ9TGn4bhiGHWftBOSDD87G7ABGnPGGVxlcqKpXWt0wjgX4z5hrUZSKcHUM\/l+wasXd7nIwRjgN7MxWAP7SEs+wEjf97epnu6tofmEexySPP\/rt9eQVLa3s1tDQO23jHz\/Gduy279uLso+AVj819bpjY6jaf0DOyp+U8p2uuBv9iyCjP3lA4L3x0MC8cQlFGtP9KODkxOVW5v3DPcOBu+Tqd5m8Lw5Q7mlETFUiolnqg6LVSPHbYywtJTvfdx2y5N5U1j\/M1xD22TP4ugiy6PuCrEFDEuR8KcHTWcDwrl8kGN\/QDMiHl2J5qagbV1zKNECME6RFWint37QxW2scHLOmTCVD6cYAH6JuV6LdgfmhPPkD7VddZ5CzkwOUiLAlyPBmxTZ02sCyjz4HsV2D5KQV2KAqxp838PYaIMN301s7\/C0EHT52YbDVbgbwdMj4T+9YEoaSBjJO6uzrDUuAEs7uWf5OP6EP\/EKYKfklEUJhg3WmrU2d9+t\/aWx\/rp0vQC9jUEx+htAbmVSnXwoljsAsn5K\/tAAka\/mBOMQxrbnQjUYwguAfqWDasONLFNY7MMf0j7eFu5NuOVbig36KMxk6J0PPodXsIg5arOdg1o70EKUjzRcznClfXCbFbrHURKdwHHTmPWt2HTq\/OFp3UX1eSg1tLw0b2N7fT8AR97AxcO+lEs\/IsgYAUrMi1EYlSz0htyvqoFtJ4QVedZIVSXM\x3d\x22,\x22AJ9oCCxFL\/rdPuriJUtZuRxfrd+YgMZ3q9U1VV66ClXFN4Fjyp4Z7PAzewg9e2sEkVP7oixqcDAqZqRObd\/3gHKtEP1llcH6\/qmToAxuqU5eAwzhZbFwzfHM8PENUwS77kdo2LlaHFRN\x22,\x22https:\/\/payments.google.com\/payments\x22,0,0,null,null,null,\x22$11.79\x22,\x22$58.99\x22,\x22$11.79\x22,\x22$58.99\x22\x5d,\x5b1,4,5\x5d,\x22IN\x22\x5d\x5d';</script><link id="favicon-link" rel="shortcut icon" href="https://ssl.gstatic.com/colaboratory-static/common/b975a0c32eb2cd1821902aeadd1622b8/img/favicon.ico"><meta name="google-site-verification" content="wRgpUU3mIRZPD1GORBPNonaotM72092B_DsqQFWNa4s"><meta name="google-site-verification" content="f5qdvL6RAXlBgHezvCLpPtvx2wU5ZgIzzPULroprlnA"><meta name="google-site-verification" content="-wL8iYJTC7X0zF9qBNDQUAd-P1ZkQUK-OhSgv4Wkf1M"><meta name="google-site-verification" content="o-EECwEDQeUpZv0jTmoGfCDX7dUI8Kul4ESepXmDnO0"><meta name="google-site-verification" content="sNOroO9gXrazN-oMODOm0Bs0_vw1R5QwZ-BfrSHn8Io"><meta name="google-site-verification" content="K1UdZBHJXQYnJGXIK1KuutmVy6dn3vG2sEyV9D1C6dM"><meta name="google-site-verification" content="wdGthzzfu0IjM3qpFqTuQL9poAQZAvAaFKyuzetLpIM"><meta name="google-site-verification" content="qZJ77guHGO0TObHUBRYVdXQlIhXBBuz8dahJVmIlzCo"><meta name="google-site-verification" content="7ahoeOOKT2ZR781GZ5xK4L9t7yO1ZOHc-gaoUALEYgw"><meta name="google-site-verification" content="PHgaSKwdxZELS21aixtLhfpvaHtKen9pnVJ25EI35Zs"><meta name="google-site-verification" content="Ozey1ptWUQW13_lCEhpPMOcmRBLqdyB3WEL-TJUjskU"><meta name="google-site-verification" content="rF5iXzWe9KZXJes1dQNhOUkS4_z_e97IrsVoCx2trek"><meta name="google-site-verification" content="z-WR3zzv8XZ5FFfBLLDbyTiN35UXm01nWUS2Uej5pwg"><meta name="google-site-verification" content="cpB5oulaGwqSxsg4E-9q2MVbK87iE9NAUUVxdveucPw"><meta name="google-site-verification" content="8P-D5fVWgUIhw8X2BxnKJbf5itK0zxX0QhoBjbJFTe8"><meta name="google-site-verification" content="88fgsZDoVRBuRnDPMIEjcHCxsEXzODOqEsJoqtvQsDc"><meta name="google-site-verification" content="sMarhZgb4va_L_7UTdMR43gDZ2gVqc_5GHN4REpQPGY"><meta name="google-site-verification" content="26aKGBCw3XblB5Ou01UhxY5WDtMqHjoTm6P-lvF6AqE"><meta name="google-site-verification" content="DGionF7db9g0dOgeBXwOAN2tmCzWBdo5yOdc_-5UcuE"><meta name="google-site-verification" content="Q9LlidR0toR7UtSyVO23xNeaqJmRp8I6r4ghBQTtntU"><meta name="google-site-verification" content="rQawcZaTEK_UrDG30cz_7nVKOVvBass61QEes0Tm04g"><meta name="google-site-verification" content="8L3ghjzKIj241AYAmEygniTe604tsXFkIrb1v-DBtGo"><meta name="google-site-verification" content="Osw7QcOK045GmOYJI2MM2_7AaL-s4q6pdn8gIv6JNxA"><meta name="google-site-verification" content="KiunYPvrY5x8umvAWcjhwPrB677xCar2LeT_8yaVrDg"><meta name="google-site-verification" content="b6bOMRzMVX2bJABYDGBPtpGcB_AUZ-o2SOTggQXErkg"><meta name="google-site-verification" content="v2MQvJk6wTiBarKTbe1mdivqYCVtw-5m6w0HDzV5X_4"><meta name="google-site-verification" content="-N1hdkiHJQ6kwJALkHVh2ZzV2fFNER0schZl2AU6zvc"><meta property="og:type" content="article"><meta property="og:image" content="https://colab.research.google.com/img/colab_favicon_256px.png"><meta property="og:title" content="Google Colab"><meta http-equiv="origin-trial" content="AmUpB2+Hlwk73pYiEMbnkef/dprJi1I9rClec33apyFsbVOaCIRN29Rk9M4ht5Otgbp+thCc3MMD73GyCNfEWAkAAAB3eyJvcmlnaW4iOiJodHRwczovL2NvbGFiLnJlc2VhcmNoLmdvb2dsZS5jb206NDQzIiwiZmVhdHVyZSI6IkRpc2FibGVUaGlyZFBhcnR5U3RvcmFnZVBhcnRpdGlvbmluZyIsImV4cGlyeSI6MTcyNTQwNzk5OX0="><script nonce="">window.performance.mark('head_end'); window.performance.measure('head', 'head_start', 'head_end');</script><script async="" src="./Task 1 - Chatbot with Rule-based responses_files/lazy.min.js.download" nonce=""></script><style id="inert-style">
[inert] {
  pointer-events: none;
  cursor: default;
}

[inert], [inert] * {
  user-select: none;
  -webkit-user-select: none;
  -moz-user-select: none;
  -ms-user-select: none;
}
</style><script async="async" type="text/javascript" src="./Task 1 - Chatbot with Rule-based responses_files/editor.main.js.download"></script><script async="" type="text/javascript" charset="UTF-8" src="./Task 1 - Chatbot with Rule-based responses_files/rs=AA2YrTt1hnGqeS6CLgm_ywEWql2sJwW4iA" nonce=""></script><link type="text/css" rel="stylesheet" href="./Task 1 - Chatbot with Rule-based responses_files/rs=AA2YrTuab1saMfPg0iiAR9TwFTm87PY2ug"><link rel="stylesheet" type="text/css" data-name="vs/editor/editor.main" href="./Task 1 - Chatbot with Rule-based responses_files/editor.main.css"><script async="async" type="text/javascript" src="./Task 1 - Chatbot with Rule-based responses_files/editor.main.nls.js.download"></script><style type="text/css">
@font-face {
  font-weight: 400;
  font-style:  normal;
  font-family: circular;

  src: url('chrome-extension://liecbddmkiiihnedobmlmillhodjkdmb/fonts/CircularXXWeb-Book.woff2') format('woff2');
}

@font-face {
  font-weight: 700;
  font-style:  normal;
  font-family: circular;

  src: url('chrome-extension://liecbddmkiiihnedobmlmillhodjkdmb/fonts/CircularXXWeb-Bold.woff2') format('woff2');
}</style><style type="text/css">.MathJax_Hover_Frame {border-radius: .25em; -webkit-border-radius: .25em; -moz-border-radius: .25em; -khtml-border-radius: .25em; box-shadow: 0px 0px 15px #83A; -webkit-box-shadow: 0px 0px 15px #83A; -moz-box-shadow: 0px 0px 15px #83A; -khtml-box-shadow: 0px 0px 15px #83A; border: 1px solid #A6D ! important; display: inline-block; position: absolute}
.MathJax_Menu_Button .MathJax_Hover_Arrow {position: absolute; cursor: pointer; display: inline-block; border: 2px solid #AAA; border-radius: 4px; -webkit-border-radius: 4px; -moz-border-radius: 4px; -khtml-border-radius: 4px; font-family: 'Courier New',Courier; font-size: 9px; color: #F0F0F0}
.MathJax_Menu_Button .MathJax_Hover_Arrow span {display: block; background-color: #AAA; border: 1px solid; border-radius: 3px; line-height: 0; padding: 4px}
.MathJax_Hover_Arrow:hover {color: white!important; border: 2px solid #CCC!important}
.MathJax_Hover_Arrow:hover span {background-color: #CCC!important}
</style><style type="text/css">#MathJax_About {position: fixed; left: 50%; width: auto; text-align: center; border: 3px outset; padding: 1em 2em; background-color: #DDDDDD; color: black; cursor: default; font-family: message-box; font-size: 120%; font-style: normal; text-indent: 0; text-transform: none; line-height: normal; letter-spacing: normal; word-spacing: normal; word-wrap: normal; white-space: nowrap; float: none; z-index: 201; border-radius: 15px; -webkit-border-radius: 15px; -moz-border-radius: 15px; -khtml-border-radius: 15px; box-shadow: 0px 10px 20px #808080; -webkit-box-shadow: 0px 10px 20px #808080; -moz-box-shadow: 0px 10px 20px #808080; -khtml-box-shadow: 0px 10px 20px #808080; filter: progid:DXImageTransform.Microsoft.dropshadow(OffX=2, OffY=2, Color='gray', Positive='true')}
#MathJax_About.MathJax_MousePost {outline: none}
.MathJax_Menu {position: absolute; background-color: white; color: black; width: auto; padding: 2px; border: 1px solid #CCCCCC; margin: 0; cursor: default; font: menu; text-align: left; text-indent: 0; text-transform: none; line-height: normal; letter-spacing: normal; word-spacing: normal; word-wrap: normal; white-space: nowrap; float: none; z-index: 201; box-shadow: 0px 10px 20px #808080; -webkit-box-shadow: 0px 10px 20px #808080; -moz-box-shadow: 0px 10px 20px #808080; -khtml-box-shadow: 0px 10px 20px #808080; filter: progid:DXImageTransform.Microsoft.dropshadow(OffX=2, OffY=2, Color='gray', Positive='true')}
.MathJax_MenuItem {padding: 2px 2em; background: transparent}
.MathJax_MenuArrow {position: absolute; right: .5em; padding-top: .25em; color: #666666; font-size: .75em}
.MathJax_MenuActive .MathJax_MenuArrow {color: white}
.MathJax_MenuArrow.RTL {left: .5em; right: auto}
.MathJax_MenuCheck {position: absolute; left: .7em}
.MathJax_MenuCheck.RTL {right: .7em; left: auto}
.MathJax_MenuRadioCheck {position: absolute; left: 1em}
.MathJax_MenuRadioCheck.RTL {right: 1em; left: auto}
.MathJax_MenuLabel {padding: 2px 2em 4px 1.33em; font-style: italic}
.MathJax_MenuRule {border-top: 1px solid #CCCCCC; margin: 4px 1px 0px}
.MathJax_MenuDisabled {color: GrayText}
.MathJax_MenuActive {background-color: Highlight; color: HighlightText}
.MathJax_MenuDisabled:focus, .MathJax_MenuLabel:focus {background-color: #E8E8E8}
.MathJax_ContextMenu:focus {outline: none}
.MathJax_ContextMenu .MathJax_MenuItem:focus {outline: none}
#MathJax_AboutClose {top: .2em; right: .2em}
.MathJax_Menu .MathJax_MenuClose {top: -10px; left: -10px}
.MathJax_MenuClose {position: absolute; cursor: pointer; display: inline-block; border: 2px solid #AAA; border-radius: 18px; -webkit-border-radius: 18px; -moz-border-radius: 18px; -khtml-border-radius: 18px; font-family: 'Courier New',Courier; font-size: 24px; color: #F0F0F0}
.MathJax_MenuClose span {display: block; background-color: #AAA; border: 1.5px solid; border-radius: 18px; -webkit-border-radius: 18px; -moz-border-radius: 18px; -khtml-border-radius: 18px; line-height: 0; padding: 8px 0 6px}
.MathJax_MenuClose:hover {color: white!important; border: 2px solid #CCC!important}
.MathJax_MenuClose:hover span {background-color: #CCC!important}
.MathJax_MenuClose:hover:focus {outline: none}
</style><style type="text/css">.MJX_Assistive_MathML {position: absolute!important; top: 0; left: 0; clip: rect(1px, 1px, 1px, 1px); padding: 1px 0 0 0!important; border: 0!important; height: 1px!important; width: 1px!important; overflow: hidden!important; display: block!important; -webkit-touch-callout: none; -webkit-user-select: none; -khtml-user-select: none; -moz-user-select: none; -ms-user-select: none; user-select: none}
.MJX_Assistive_MathML.MJX_Assistive_MathML_Block {width: 100%!important}
</style><style type="text/css">#MathJax_Zoom {position: absolute; background-color: #F0F0F0; overflow: auto; display: block; z-index: 301; padding: .5em; border: 1px solid black; margin: 0; font-weight: normal; font-style: normal; text-align: left; text-indent: 0; text-transform: none; line-height: normal; letter-spacing: normal; word-spacing: normal; word-wrap: normal; white-space: nowrap; float: none; -webkit-box-sizing: content-box; -moz-box-sizing: content-box; box-sizing: content-box; box-shadow: 5px 5px 15px #AAAAAA; -webkit-box-shadow: 5px 5px 15px #AAAAAA; -moz-box-shadow: 5px 5px 15px #AAAAAA; -khtml-box-shadow: 5px 5px 15px #AAAAAA; filter: progid:DXImageTransform.Microsoft.dropshadow(OffX=2, OffY=2, Color='gray', Positive='true')}
#MathJax_ZoomOverlay {position: absolute; left: 0; top: 0; z-index: 300; display: inline-block; width: 100%; height: 100%; border: 0; padding: 0; margin: 0; background-color: white; opacity: 0; filter: alpha(opacity=0)}
#MathJax_ZoomFrame {position: relative; display: inline-block; height: 0; width: 0}
#MathJax_ZoomEventTrap {position: absolute; left: 0; top: 0; z-index: 302; display: inline-block; border: 0; padding: 0; margin: 0; background-color: white; opacity: 0; filter: alpha(opacity=0)}
</style><style type="text/css">.MathJax_Preview {color: #888}
#MathJax_Message {position: fixed; left: 1em; bottom: 1.5em; background-color: #E6E6E6; border: 1px solid #959595; margin: 0px; padding: 2px 8px; z-index: 102; color: black; font-size: 80%; width: auto; white-space: nowrap}
#MathJax_MSIE_Frame {position: absolute; top: 0; left: 0; width: 0px; z-index: 101; border: 0px; margin: 0px; padding: 0px}
.MathJax_Error {color: #CC0000; font-style: italic}
</style><style type="text/css">.MJXp-script {font-size: .8em}
.MJXp-right {-webkit-transform-origin: right; -moz-transform-origin: right; -ms-transform-origin: right; -o-transform-origin: right; transform-origin: right}
.MJXp-bold {font-weight: bold}
.MJXp-italic {font-style: italic}
.MJXp-scr {font-family: MathJax_Script,'Times New Roman',Times,STIXGeneral,serif}
.MJXp-frak {font-family: MathJax_Fraktur,'Times New Roman',Times,STIXGeneral,serif}
.MJXp-sf {font-family: MathJax_SansSerif,'Times New Roman',Times,STIXGeneral,serif}
.MJXp-cal {font-family: MathJax_Caligraphic,'Times New Roman',Times,STIXGeneral,serif}
.MJXp-mono {font-family: MathJax_Typewriter,'Times New Roman',Times,STIXGeneral,serif}
.MJXp-largeop {font-size: 150%}
.MJXp-largeop.MJXp-int {vertical-align: -.2em}
.MJXp-math {display: inline-block; line-height: 1.2; text-indent: 0; font-family: 'Times New Roman',Times,STIXGeneral,serif; white-space: nowrap; border-collapse: collapse}
.MJXp-display {display: block; text-align: center; margin: 1em 0}
.MJXp-math span {display: inline-block}
.MJXp-box {display: block!important; text-align: center}
.MJXp-box:after {content: " "}
.MJXp-rule {display: block!important; margin-top: .1em}
.MJXp-char {display: block!important}
.MJXp-mo {margin: 0 .15em}
.MJXp-mfrac {margin: 0 .125em; vertical-align: .25em}
.MJXp-denom {display: inline-table!important; width: 100%}
.MJXp-denom > * {display: table-row!important}
.MJXp-surd {vertical-align: top}
.MJXp-surd > * {display: block!important}
.MJXp-script-box > *  {display: table!important; height: 50%}
.MJXp-script-box > * > * {display: table-cell!important; vertical-align: top}
.MJXp-script-box > *:last-child > * {vertical-align: bottom}
.MJXp-script-box > * > * > * {display: block!important}
.MJXp-mphantom {visibility: hidden}
.MJXp-munderover, .MJXp-munder {display: inline-table!important}
.MJXp-over {display: inline-block!important; text-align: center}
.MJXp-over > * {display: block!important}
.MJXp-munderover > *, .MJXp-munder > * {display: table-row!important}
.MJXp-mtable {vertical-align: .25em; margin: 0 .125em}
.MJXp-mtable > * {display: inline-table!important; vertical-align: middle}
.MJXp-mtr {display: table-row!important}
.MJXp-mtd {display: table-cell!important; text-align: center; padding: .5em 0 0 .5em}
.MJXp-mtr > .MJXp-mtd:first-child {padding-left: 0}
.MJXp-mtr:first-child > .MJXp-mtd {padding-top: 0}
.MJXp-mlabeledtr {display: table-row!important}
.MJXp-mlabeledtr > .MJXp-mtd:first-child {padding-left: 0}
.MJXp-mlabeledtr:first-child > .MJXp-mtd {padding-top: 0}
.MJXp-merror {background-color: #FFFF88; color: #CC0000; border: 1px solid #CC0000; padding: 1px 3px; font-style: normal; font-size: 90%}
.MJXp-scale0 {-webkit-transform: scaleX(.0); -moz-transform: scaleX(.0); -ms-transform: scaleX(.0); -o-transform: scaleX(.0); transform: scaleX(.0)}
.MJXp-scale1 {-webkit-transform: scaleX(.1); -moz-transform: scaleX(.1); -ms-transform: scaleX(.1); -o-transform: scaleX(.1); transform: scaleX(.1)}
.MJXp-scale2 {-webkit-transform: scaleX(.2); -moz-transform: scaleX(.2); -ms-transform: scaleX(.2); -o-transform: scaleX(.2); transform: scaleX(.2)}
.MJXp-scale3 {-webkit-transform: scaleX(.3); -moz-transform: scaleX(.3); -ms-transform: scaleX(.3); -o-transform: scaleX(.3); transform: scaleX(.3)}
.MJXp-scale4 {-webkit-transform: scaleX(.4); -moz-transform: scaleX(.4); -ms-transform: scaleX(.4); -o-transform: scaleX(.4); transform: scaleX(.4)}
.MJXp-scale5 {-webkit-transform: scaleX(.5); -moz-transform: scaleX(.5); -ms-transform: scaleX(.5); -o-transform: scaleX(.5); transform: scaleX(.5)}
.MJXp-scale6 {-webkit-transform: scaleX(.6); -moz-transform: scaleX(.6); -ms-transform: scaleX(.6); -o-transform: scaleX(.6); transform: scaleX(.6)}
.MJXp-scale7 {-webkit-transform: scaleX(.7); -moz-transform: scaleX(.7); -ms-transform: scaleX(.7); -o-transform: scaleX(.7); transform: scaleX(.7)}
.MJXp-scale8 {-webkit-transform: scaleX(.8); -moz-transform: scaleX(.8); -ms-transform: scaleX(.8); -o-transform: scaleX(.8); transform: scaleX(.8)}
.MJXp-scale9 {-webkit-transform: scaleX(.9); -moz-transform: scaleX(.9); -ms-transform: scaleX(.9); -o-transform: scaleX(.9); transform: scaleX(.9)}
.MathJax_PHTML .noError {vertical-align: ; font-size: 90%; text-align: left; color: black; padding: 1px 3px; border: 1px solid}
</style><script src="./Task 1 - Chatbot with Rule-based responses_files/api.js.download" nonce=""></script><script src="./Task 1 - Chatbot with Rule-based responses_files/api(1).js.download" nonce=""></script><style type="text/css" media="screen" class="monaco-colors">.codicon-add:before { content: '\ea60'; }
.codicon-plus:before { content: '\ea60'; }
.codicon-gist-new:before { content: '\ea60'; }
.codicon-repo-create:before { content: '\ea60'; }
.codicon-lightbulb:before { content: '\ea61'; }
.codicon-light-bulb:before { content: '\ea61'; }
.codicon-repo:before { content: '\ea62'; }
.codicon-repo-delete:before { content: '\ea62'; }
.codicon-gist-fork:before { content: '\ea63'; }
.codicon-repo-forked:before { content: '\ea63'; }
.codicon-git-pull-request:before { content: '\ea64'; }
.codicon-git-pull-request-abandoned:before { content: '\ea64'; }
.codicon-record-keys:before { content: '\ea65'; }
.codicon-keyboard:before { content: '\ea65'; }
.codicon-tag:before { content: '\ea66'; }
.codicon-tag-add:before { content: '\ea66'; }
.codicon-tag-remove:before { content: '\ea66'; }
.codicon-person:before { content: '\ea67'; }
.codicon-person-follow:before { content: '\ea67'; }
.codicon-person-outline:before { content: '\ea67'; }
.codicon-person-filled:before { content: '\ea67'; }
.codicon-git-branch:before { content: '\ea68'; }
.codicon-git-branch-create:before { content: '\ea68'; }
.codicon-git-branch-delete:before { content: '\ea68'; }
.codicon-source-control:before { content: '\ea68'; }
.codicon-mirror:before { content: '\ea69'; }
.codicon-mirror-public:before { content: '\ea69'; }
.codicon-star:before { content: '\ea6a'; }
.codicon-star-add:before { content: '\ea6a'; }
.codicon-star-delete:before { content: '\ea6a'; }
.codicon-star-empty:before { content: '\ea6a'; }
.codicon-comment:before { content: '\ea6b'; }
.codicon-comment-add:before { content: '\ea6b'; }
.codicon-alert:before { content: '\ea6c'; }
.codicon-warning:before { content: '\ea6c'; }
.codicon-search:before { content: '\ea6d'; }
.codicon-search-save:before { content: '\ea6d'; }
.codicon-log-out:before { content: '\ea6e'; }
.codicon-sign-out:before { content: '\ea6e'; }
.codicon-log-in:before { content: '\ea6f'; }
.codicon-sign-in:before { content: '\ea6f'; }
.codicon-eye:before { content: '\ea70'; }
.codicon-eye-unwatch:before { content: '\ea70'; }
.codicon-eye-watch:before { content: '\ea70'; }
.codicon-circle-filled:before { content: '\ea71'; }
.codicon-primitive-dot:before { content: '\ea71'; }
.codicon-close-dirty:before { content: '\ea71'; }
.codicon-debug-breakpoint:before { content: '\ea71'; }
.codicon-debug-breakpoint-disabled:before { content: '\ea71'; }
.codicon-debug-hint:before { content: '\ea71'; }
.codicon-primitive-square:before { content: '\ea72'; }
.codicon-edit:before { content: '\ea73'; }
.codicon-pencil:before { content: '\ea73'; }
.codicon-info:before { content: '\ea74'; }
.codicon-issue-opened:before { content: '\ea74'; }
.codicon-gist-private:before { content: '\ea75'; }
.codicon-git-fork-private:before { content: '\ea75'; }
.codicon-lock:before { content: '\ea75'; }
.codicon-mirror-private:before { content: '\ea75'; }
.codicon-close:before { content: '\ea76'; }
.codicon-remove-close:before { content: '\ea76'; }
.codicon-x:before { content: '\ea76'; }
.codicon-repo-sync:before { content: '\ea77'; }
.codicon-sync:before { content: '\ea77'; }
.codicon-clone:before { content: '\ea78'; }
.codicon-desktop-download:before { content: '\ea78'; }
.codicon-beaker:before { content: '\ea79'; }
.codicon-microscope:before { content: '\ea79'; }
.codicon-vm:before { content: '\ea7a'; }
.codicon-device-desktop:before { content: '\ea7a'; }
.codicon-file:before { content: '\ea7b'; }
.codicon-file-text:before { content: '\ea7b'; }
.codicon-more:before { content: '\ea7c'; }
.codicon-ellipsis:before { content: '\ea7c'; }
.codicon-kebab-horizontal:before { content: '\ea7c'; }
.codicon-mail-reply:before { content: '\ea7d'; }
.codicon-reply:before { content: '\ea7d'; }
.codicon-organization:before { content: '\ea7e'; }
.codicon-organization-filled:before { content: '\ea7e'; }
.codicon-organization-outline:before { content: '\ea7e'; }
.codicon-new-file:before { content: '\ea7f'; }
.codicon-file-add:before { content: '\ea7f'; }
.codicon-new-folder:before { content: '\ea80'; }
.codicon-file-directory-create:before { content: '\ea80'; }
.codicon-trash:before { content: '\ea81'; }
.codicon-trashcan:before { content: '\ea81'; }
.codicon-history:before { content: '\ea82'; }
.codicon-clock:before { content: '\ea82'; }
.codicon-folder:before { content: '\ea83'; }
.codicon-file-directory:before { content: '\ea83'; }
.codicon-symbol-folder:before { content: '\ea83'; }
.codicon-logo-github:before { content: '\ea84'; }
.codicon-mark-github:before { content: '\ea84'; }
.codicon-github:before { content: '\ea84'; }
.codicon-terminal:before { content: '\ea85'; }
.codicon-console:before { content: '\ea85'; }
.codicon-repl:before { content: '\ea85'; }
.codicon-zap:before { content: '\ea86'; }
.codicon-symbol-event:before { content: '\ea86'; }
.codicon-error:before { content: '\ea87'; }
.codicon-stop:before { content: '\ea87'; }
.codicon-variable:before { content: '\ea88'; }
.codicon-symbol-variable:before { content: '\ea88'; }
.codicon-array:before { content: '\ea8a'; }
.codicon-symbol-array:before { content: '\ea8a'; }
.codicon-symbol-module:before { content: '\ea8b'; }
.codicon-symbol-package:before { content: '\ea8b'; }
.codicon-symbol-namespace:before { content: '\ea8b'; }
.codicon-symbol-object:before { content: '\ea8b'; }
.codicon-symbol-method:before { content: '\ea8c'; }
.codicon-symbol-function:before { content: '\ea8c'; }
.codicon-symbol-constructor:before { content: '\ea8c'; }
.codicon-symbol-boolean:before { content: '\ea8f'; }
.codicon-symbol-null:before { content: '\ea8f'; }
.codicon-symbol-numeric:before { content: '\ea90'; }
.codicon-symbol-number:before { content: '\ea90'; }
.codicon-symbol-structure:before { content: '\ea91'; }
.codicon-symbol-struct:before { content: '\ea91'; }
.codicon-symbol-parameter:before { content: '\ea92'; }
.codicon-symbol-type-parameter:before { content: '\ea92'; }
.codicon-symbol-key:before { content: '\ea93'; }
.codicon-symbol-text:before { content: '\ea93'; }
.codicon-symbol-reference:before { content: '\ea94'; }
.codicon-go-to-file:before { content: '\ea94'; }
.codicon-symbol-enum:before { content: '\ea95'; }
.codicon-symbol-value:before { content: '\ea95'; }
.codicon-symbol-ruler:before { content: '\ea96'; }
.codicon-symbol-unit:before { content: '\ea96'; }
.codicon-activate-breakpoints:before { content: '\ea97'; }
.codicon-archive:before { content: '\ea98'; }
.codicon-arrow-both:before { content: '\ea99'; }
.codicon-arrow-down:before { content: '\ea9a'; }
.codicon-arrow-left:before { content: '\ea9b'; }
.codicon-arrow-right:before { content: '\ea9c'; }
.codicon-arrow-small-down:before { content: '\ea9d'; }
.codicon-arrow-small-left:before { content: '\ea9e'; }
.codicon-arrow-small-right:before { content: '\ea9f'; }
.codicon-arrow-small-up:before { content: '\eaa0'; }
.codicon-arrow-up:before { content: '\eaa1'; }
.codicon-bell:before { content: '\eaa2'; }
.codicon-bold:before { content: '\eaa3'; }
.codicon-book:before { content: '\eaa4'; }
.codicon-bookmark:before { content: '\eaa5'; }
.codicon-debug-breakpoint-conditional-unverified:before { content: '\eaa6'; }
.codicon-debug-breakpoint-conditional:before { content: '\eaa7'; }
.codicon-debug-breakpoint-conditional-disabled:before { content: '\eaa7'; }
.codicon-debug-breakpoint-data-unverified:before { content: '\eaa8'; }
.codicon-debug-breakpoint-data:before { content: '\eaa9'; }
.codicon-debug-breakpoint-data-disabled:before { content: '\eaa9'; }
.codicon-debug-breakpoint-log-unverified:before { content: '\eaaa'; }
.codicon-debug-breakpoint-log:before { content: '\eaab'; }
.codicon-debug-breakpoint-log-disabled:before { content: '\eaab'; }
.codicon-briefcase:before { content: '\eaac'; }
.codicon-broadcast:before { content: '\eaad'; }
.codicon-browser:before { content: '\eaae'; }
.codicon-bug:before { content: '\eaaf'; }
.codicon-calendar:before { content: '\eab0'; }
.codicon-case-sensitive:before { content: '\eab1'; }
.codicon-check:before { content: '\eab2'; }
.codicon-checklist:before { content: '\eab3'; }
.codicon-chevron-down:before { content: '\eab4'; }
.codicon-drop-down-button:before { content: '\eab4'; }
.codicon-chevron-left:before { content: '\eab5'; }
.codicon-chevron-right:before { content: '\eab6'; }
.codicon-chevron-up:before { content: '\eab7'; }
.codicon-chrome-close:before { content: '\eab8'; }
.codicon-chrome-maximize:before { content: '\eab9'; }
.codicon-chrome-minimize:before { content: '\eaba'; }
.codicon-chrome-restore:before { content: '\eabb'; }
.codicon-circle:before { content: '\eabc'; }
.codicon-circle-outline:before { content: '\eabc'; }
.codicon-debug-breakpoint-unverified:before { content: '\eabc'; }
.codicon-circle-slash:before { content: '\eabd'; }
.codicon-circuit-board:before { content: '\eabe'; }
.codicon-clear-all:before { content: '\eabf'; }
.codicon-clippy:before { content: '\eac0'; }
.codicon-close-all:before { content: '\eac1'; }
.codicon-cloud-download:before { content: '\eac2'; }
.codicon-cloud-upload:before { content: '\eac3'; }
.codicon-code:before { content: '\eac4'; }
.codicon-collapse-all:before { content: '\eac5'; }
.codicon-color-mode:before { content: '\eac6'; }
.codicon-comment-discussion:before { content: '\eac7'; }
.codicon-compare-changes:before { content: '\eafd'; }
.codicon-credit-card:before { content: '\eac9'; }
.codicon-dash:before { content: '\eacc'; }
.codicon-dashboard:before { content: '\eacd'; }
.codicon-database:before { content: '\eace'; }
.codicon-debug-continue:before { content: '\eacf'; }
.codicon-debug-disconnect:before { content: '\ead0'; }
.codicon-debug-pause:before { content: '\ead1'; }
.codicon-debug-restart:before { content: '\ead2'; }
.codicon-debug-start:before { content: '\ead3'; }
.codicon-debug-step-into:before { content: '\ead4'; }
.codicon-debug-step-out:before { content: '\ead5'; }
.codicon-debug-step-over:before { content: '\ead6'; }
.codicon-debug-stop:before { content: '\ead7'; }
.codicon-debug:before { content: '\ead8'; }
.codicon-device-camera-video:before { content: '\ead9'; }
.codicon-device-camera:before { content: '\eada'; }
.codicon-device-mobile:before { content: '\eadb'; }
.codicon-diff-added:before { content: '\eadc'; }
.codicon-diff-ignored:before { content: '\eadd'; }
.codicon-diff-modified:before { content: '\eade'; }
.codicon-diff-removed:before { content: '\eadf'; }
.codicon-diff-renamed:before { content: '\eae0'; }
.codicon-diff:before { content: '\eae1'; }
.codicon-discard:before { content: '\eae2'; }
.codicon-editor-layout:before { content: '\eae3'; }
.codicon-empty-window:before { content: '\eae4'; }
.codicon-exclude:before { content: '\eae5'; }
.codicon-extensions:before { content: '\eae6'; }
.codicon-eye-closed:before { content: '\eae7'; }
.codicon-file-binary:before { content: '\eae8'; }
.codicon-file-code:before { content: '\eae9'; }
.codicon-file-media:before { content: '\eaea'; }
.codicon-file-pdf:before { content: '\eaeb'; }
.codicon-file-submodule:before { content: '\eaec'; }
.codicon-file-symlink-directory:before { content: '\eaed'; }
.codicon-file-symlink-file:before { content: '\eaee'; }
.codicon-file-zip:before { content: '\eaef'; }
.codicon-files:before { content: '\eaf0'; }
.codicon-filter:before { content: '\eaf1'; }
.codicon-flame:before { content: '\eaf2'; }
.codicon-fold-down:before { content: '\eaf3'; }
.codicon-fold-up:before { content: '\eaf4'; }
.codicon-fold:before { content: '\eaf5'; }
.codicon-folder-active:before { content: '\eaf6'; }
.codicon-folder-opened:before { content: '\eaf7'; }
.codicon-gear:before { content: '\eaf8'; }
.codicon-gift:before { content: '\eaf9'; }
.codicon-gist-secret:before { content: '\eafa'; }
.codicon-gist:before { content: '\eafb'; }
.codicon-git-commit:before { content: '\eafc'; }
.codicon-git-compare:before { content: '\eafd'; }
.codicon-git-merge:before { content: '\eafe'; }
.codicon-github-action:before { content: '\eaff'; }
.codicon-github-alt:before { content: '\eb00'; }
.codicon-globe:before { content: '\eb01'; }
.codicon-grabber:before { content: '\eb02'; }
.codicon-graph:before { content: '\eb03'; }
.codicon-gripper:before { content: '\eb04'; }
.codicon-heart:before { content: '\eb05'; }
.codicon-home:before { content: '\eb06'; }
.codicon-horizontal-rule:before { content: '\eb07'; }
.codicon-hubot:before { content: '\eb08'; }
.codicon-inbox:before { content: '\eb09'; }
.codicon-issue-closed:before { content: '\eba4'; }
.codicon-issue-reopened:before { content: '\eb0b'; }
.codicon-issues:before { content: '\eb0c'; }
.codicon-italic:before { content: '\eb0d'; }
.codicon-jersey:before { content: '\eb0e'; }
.codicon-json:before { content: '\eb0f'; }
.codicon-bracket:before { content: '\eb0f'; }
.codicon-kebab-vertical:before { content: '\eb10'; }
.codicon-key:before { content: '\eb11'; }
.codicon-law:before { content: '\eb12'; }
.codicon-lightbulb-autofix:before { content: '\eb13'; }
.codicon-link-external:before { content: '\eb14'; }
.codicon-link:before { content: '\eb15'; }
.codicon-list-ordered:before { content: '\eb16'; }
.codicon-list-unordered:before { content: '\eb17'; }
.codicon-live-share:before { content: '\eb18'; }
.codicon-loading:before { content: '\eb19'; }
.codicon-location:before { content: '\eb1a'; }
.codicon-mail-read:before { content: '\eb1b'; }
.codicon-mail:before { content: '\eb1c'; }
.codicon-markdown:before { content: '\eb1d'; }
.codicon-megaphone:before { content: '\eb1e'; }
.codicon-mention:before { content: '\eb1f'; }
.codicon-milestone:before { content: '\eb20'; }
.codicon-mortar-board:before { content: '\eb21'; }
.codicon-move:before { content: '\eb22'; }
.codicon-multiple-windows:before { content: '\eb23'; }
.codicon-mute:before { content: '\eb24'; }
.codicon-no-newline:before { content: '\eb25'; }
.codicon-note:before { content: '\eb26'; }
.codicon-octoface:before { content: '\eb27'; }
.codicon-open-preview:before { content: '\eb28'; }
.codicon-package:before { content: '\eb29'; }
.codicon-paintcan:before { content: '\eb2a'; }
.codicon-pin:before { content: '\eb2b'; }
.codicon-play:before { content: '\eb2c'; }
.codicon-run:before { content: '\eb2c'; }
.codicon-plug:before { content: '\eb2d'; }
.codicon-preserve-case:before { content: '\eb2e'; }
.codicon-preview:before { content: '\eb2f'; }
.codicon-project:before { content: '\eb30'; }
.codicon-pulse:before { content: '\eb31'; }
.codicon-question:before { content: '\eb32'; }
.codicon-quote:before { content: '\eb33'; }
.codicon-radio-tower:before { content: '\eb34'; }
.codicon-reactions:before { content: '\eb35'; }
.codicon-references:before { content: '\eb36'; }
.codicon-refresh:before { content: '\eb37'; }
.codicon-regex:before { content: '\eb38'; }
.codicon-remote-explorer:before { content: '\eb39'; }
.codicon-remote:before { content: '\eb3a'; }
.codicon-remove:before { content: '\eb3b'; }
.codicon-replace-all:before { content: '\eb3c'; }
.codicon-replace:before { content: '\eb3d'; }
.codicon-repo-clone:before { content: '\eb3e'; }
.codicon-repo-force-push:before { content: '\eb3f'; }
.codicon-repo-pull:before { content: '\eb40'; }
.codicon-repo-push:before { content: '\eb41'; }
.codicon-report:before { content: '\eb42'; }
.codicon-request-changes:before { content: '\eb43'; }
.codicon-rocket:before { content: '\eb44'; }
.codicon-root-folder-opened:before { content: '\eb45'; }
.codicon-root-folder:before { content: '\eb46'; }
.codicon-rss:before { content: '\eb47'; }
.codicon-ruby:before { content: '\eb48'; }
.codicon-save-all:before { content: '\eb49'; }
.codicon-save-as:before { content: '\eb4a'; }
.codicon-save:before { content: '\eb4b'; }
.codicon-screen-full:before { content: '\eb4c'; }
.codicon-screen-normal:before { content: '\eb4d'; }
.codicon-search-stop:before { content: '\eb4e'; }
.codicon-server:before { content: '\eb50'; }
.codicon-settings-gear:before { content: '\eb51'; }
.codicon-settings:before { content: '\eb52'; }
.codicon-shield:before { content: '\eb53'; }
.codicon-smiley:before { content: '\eb54'; }
.codicon-sort-precedence:before { content: '\eb55'; }
.codicon-split-horizontal:before { content: '\eb56'; }
.codicon-split-vertical:before { content: '\eb57'; }
.codicon-squirrel:before { content: '\eb58'; }
.codicon-star-full:before { content: '\eb59'; }
.codicon-star-half:before { content: '\eb5a'; }
.codicon-symbol-class:before { content: '\eb5b'; }
.codicon-symbol-color:before { content: '\eb5c'; }
.codicon-symbol-customcolor:before { content: '\eb5c'; }
.codicon-symbol-constant:before { content: '\eb5d'; }
.codicon-symbol-enum-member:before { content: '\eb5e'; }
.codicon-symbol-field:before { content: '\eb5f'; }
.codicon-symbol-file:before { content: '\eb60'; }
.codicon-symbol-interface:before { content: '\eb61'; }
.codicon-symbol-keyword:before { content: '\eb62'; }
.codicon-symbol-misc:before { content: '\eb63'; }
.codicon-symbol-operator:before { content: '\eb64'; }
.codicon-symbol-property:before { content: '\eb65'; }
.codicon-wrench:before { content: '\eb65'; }
.codicon-wrench-subaction:before { content: '\eb65'; }
.codicon-symbol-snippet:before { content: '\eb66'; }
.codicon-tasklist:before { content: '\eb67'; }
.codicon-telescope:before { content: '\eb68'; }
.codicon-text-size:before { content: '\eb69'; }
.codicon-three-bars:before { content: '\eb6a'; }
.codicon-thumbsdown:before { content: '\eb6b'; }
.codicon-thumbsup:before { content: '\eb6c'; }
.codicon-tools:before { content: '\eb6d'; }
.codicon-triangle-down:before { content: '\eb6e'; }
.codicon-triangle-left:before { content: '\eb6f'; }
.codicon-triangle-right:before { content: '\eb70'; }
.codicon-triangle-up:before { content: '\eb71'; }
.codicon-twitter:before { content: '\eb72'; }
.codicon-unfold:before { content: '\eb73'; }
.codicon-unlock:before { content: '\eb74'; }
.codicon-unmute:before { content: '\eb75'; }
.codicon-unverified:before { content: '\eb76'; }
.codicon-verified:before { content: '\eb77'; }
.codicon-versions:before { content: '\eb78'; }
.codicon-vm-active:before { content: '\eb79'; }
.codicon-vm-outline:before { content: '\eb7a'; }
.codicon-vm-running:before { content: '\eb7b'; }
.codicon-watch:before { content: '\eb7c'; }
.codicon-whitespace:before { content: '\eb7d'; }
.codicon-whole-word:before { content: '\eb7e'; }
.codicon-window:before { content: '\eb7f'; }
.codicon-word-wrap:before { content: '\eb80'; }
.codicon-zoom-in:before { content: '\eb81'; }
.codicon-zoom-out:before { content: '\eb82'; }
.codicon-list-filter:before { content: '\eb83'; }
.codicon-list-flat:before { content: '\eb84'; }
.codicon-list-selection:before { content: '\eb85'; }
.codicon-selection:before { content: '\eb85'; }
.codicon-list-tree:before { content: '\eb86'; }
.codicon-debug-breakpoint-function-unverified:before { content: '\eb87'; }
.codicon-debug-breakpoint-function:before { content: '\eb88'; }
.codicon-debug-breakpoint-function-disabled:before { content: '\eb88'; }
.codicon-debug-stackframe-active:before { content: '\eb89'; }
.codicon-circle-small-filled:before { content: '\eb8a'; }
.codicon-debug-stackframe-dot:before { content: '\eb8a'; }
.codicon-debug-stackframe:before { content: '\eb8b'; }
.codicon-debug-stackframe-focused:before { content: '\eb8b'; }
.codicon-debug-breakpoint-unsupported:before { content: '\eb8c'; }
.codicon-symbol-string:before { content: '\eb8d'; }
.codicon-debug-reverse-continue:before { content: '\eb8e'; }
.codicon-debug-step-back:before { content: '\eb8f'; }
.codicon-debug-restart-frame:before { content: '\eb90'; }
.codicon-call-incoming:before { content: '\eb92'; }
.codicon-call-outgoing:before { content: '\eb93'; }
.codicon-menu:before { content: '\eb94'; }
.codicon-expand-all:before { content: '\eb95'; }
.codicon-feedback:before { content: '\eb96'; }
.codicon-group-by-ref-type:before { content: '\eb97'; }
.codicon-ungroup-by-ref-type:before { content: '\eb98'; }
.codicon-account:before { content: '\eb99'; }
.codicon-bell-dot:before { content: '\eb9a'; }
.codicon-debug-console:before { content: '\eb9b'; }
.codicon-library:before { content: '\eb9c'; }
.codicon-output:before { content: '\eb9d'; }
.codicon-run-all:before { content: '\eb9e'; }
.codicon-sync-ignored:before { content: '\eb9f'; }
.codicon-pinned:before { content: '\eba0'; }
.codicon-github-inverted:before { content: '\eba1'; }
.codicon-debug-alt:before { content: '\eb91'; }
.codicon-server-process:before { content: '\eba2'; }
.codicon-server-environment:before { content: '\eba3'; }
.codicon-pass:before { content: '\eba4'; }
.codicon-stop-circle:before { content: '\eba5'; }
.codicon-play-circle:before { content: '\eba6'; }
.codicon-record:before { content: '\eba7'; }
.codicon-debug-alt-small:before { content: '\eba8'; }
.codicon-vm-connect:before { content: '\eba9'; }
.codicon-cloud:before { content: '\ebaa'; }
.codicon-merge:before { content: '\ebab'; }
.codicon-export:before { content: '\ebac'; }
.codicon-graph-left:before { content: '\ebad'; }
.codicon-magnet:before { content: '\ebae'; }
.codicon-notebook:before { content: '\ebaf'; }
.codicon-redo:before { content: '\ebb0'; }
.codicon-check-all:before { content: '\ebb1'; }
.codicon-pinned-dirty:before { content: '\ebb2'; }
.codicon-pass-filled:before { content: '\ebb3'; }
.codicon-circle-large-filled:before { content: '\ebb4'; }
.codicon-circle-large:before { content: '\ebb5'; }
.codicon-circle-large-outline:before { content: '\ebb5'; }
.codicon-combine:before { content: '\ebb6'; }
.codicon-gather:before { content: '\ebb6'; }
.codicon-table:before { content: '\ebb7'; }
.codicon-variable-group:before { content: '\ebb8'; }
.codicon-type-hierarchy:before { content: '\ebb9'; }
.codicon-type-hierarchy-sub:before { content: '\ebba'; }
.codicon-type-hierarchy-super:before { content: '\ebbb'; }
.codicon-git-pull-request-create:before { content: '\ebbc'; }
.codicon-run-above:before { content: '\ebbd'; }
.codicon-run-below:before { content: '\ebbe'; }
.codicon-notebook-template:before { content: '\ebbf'; }
.codicon-debug-rerun:before { content: '\ebc0'; }
.codicon-workspace-trusted:before { content: '\ebc1'; }
.codicon-workspace-untrusted:before { content: '\ebc2'; }
.codicon-workspace-unspecified:before { content: '\ebc3'; }
.codicon-terminal-cmd:before { content: '\ebc4'; }
.codicon-terminal-debian:before { content: '\ebc5'; }
.codicon-terminal-linux:before { content: '\ebc6'; }
.codicon-terminal-powershell:before { content: '\ebc7'; }
.codicon-terminal-tmux:before { content: '\ebc8'; }
.codicon-terminal-ubuntu:before { content: '\ebc9'; }
.codicon-terminal-bash:before { content: '\ebca'; }
.codicon-arrow-swap:before { content: '\ebcb'; }
.codicon-copy:before { content: '\ebcc'; }
.codicon-person-add:before { content: '\ebcd'; }
.codicon-filter-filled:before { content: '\ebce'; }
.codicon-wand:before { content: '\ebcf'; }
.codicon-debug-line-by-line:before { content: '\ebd0'; }
.codicon-inspect:before { content: '\ebd1'; }
.codicon-layers:before { content: '\ebd2'; }
.codicon-layers-dot:before { content: '\ebd3'; }
.codicon-layers-active:before { content: '\ebd4'; }
.codicon-compass:before { content: '\ebd5'; }
.codicon-compass-dot:before { content: '\ebd6'; }
.codicon-compass-active:before { content: '\ebd7'; }
.codicon-azure:before { content: '\ebd8'; }
.codicon-issue-draft:before { content: '\ebd9'; }
.codicon-git-pull-request-closed:before { content: '\ebda'; }
.codicon-git-pull-request-draft:before { content: '\ebdb'; }
.codicon-debug-all:before { content: '\ebdc'; }
.codicon-debug-coverage:before { content: '\ebdd'; }
.codicon-run-errors:before { content: '\ebde'; }
.codicon-folder-library:before { content: '\ebdf'; }
.codicon-debug-continue-small:before { content: '\ebe0'; }
.codicon-beaker-stop:before { content: '\ebe1'; }
.codicon-graph-line:before { content: '\ebe2'; }
.codicon-graph-scatter:before { content: '\ebe3'; }
.codicon-pie-chart:before { content: '\ebe4'; }
.codicon-bracket-dot:before { content: '\ebe5'; }
.codicon-bracket-error:before { content: '\ebe6'; }
.codicon-lock-small:before { content: '\ebe7'; }
.codicon-azure-devops:before { content: '\ebe8'; }
.codicon-verified-filled:before { content: '\ebe9'; }
.codicon-newline:before { content: '\ebea'; }
.codicon-layout:before { content: '\ebeb'; }
.codicon-layout-activitybar-left:before { content: '\ebec'; }
.codicon-layout-activitybar-right:before { content: '\ebed'; }
.codicon-layout-panel-left:before { content: '\ebee'; }
.codicon-layout-panel-center:before { content: '\ebef'; }
.codicon-layout-panel-justify:before { content: '\ebf0'; }
.codicon-layout-panel-right:before { content: '\ebf1'; }
.codicon-layout-panel:before { content: '\ebf2'; }
.codicon-layout-sidebar-left:before { content: '\ebf3'; }
.codicon-layout-sidebar-right:before { content: '\ebf4'; }
.codicon-layout-statusbar:before { content: '\ebf5'; }
.codicon-layout-menubar:before { content: '\ebf6'; }
.codicon-layout-centered:before { content: '\ebf7'; }
.codicon-layout-sidebar-right-off:before { content: '\ec00'; }
.codicon-layout-panel-off:before { content: '\ec01'; }
.codicon-layout-sidebar-left-off:before { content: '\ec02'; }
.codicon-target:before { content: '\ebf8'; }
.codicon-indent:before { content: '\ebf9'; }
.codicon-record-small:before { content: '\ebfa'; }
.codicon-error-small:before { content: '\ebfb'; }
.codicon-arrow-circle-down:before { content: '\ebfc'; }
.codicon-arrow-circle-left:before { content: '\ebfd'; }
.codicon-arrow-circle-right:before { content: '\ebfe'; }
.codicon-arrow-circle-up:before { content: '\ebff'; }
.codicon-heart-filled:before { content: '\ec04'; }
.codicon-map:before { content: '\ec05'; }
.codicon-map-filled:before { content: '\ec06'; }
.codicon-circle-small:before { content: '\ec07'; }
.codicon-bell-slash:before { content: '\ec08'; }
.codicon-bell-slash-dot:before { content: '\ec09'; }
.codicon-comment-unresolved:before { content: '\ec0a'; }
.codicon-git-pull-request-go-to-changes:before { content: '\ec0b'; }
.codicon-git-pull-request-new-changes:before { content: '\ec0c'; }
.codicon-search-fuzzy:before { content: '\ec0d'; }
.codicon-comment-draft:before { content: '\ec0e'; }
.codicon-send:before { content: '\ec0f'; }
.codicon-sparkle:before { content: '\ec10'; }
.codicon-insert:before { content: '\ec11'; }
.codicon-dialog-error:before { content: '\ea87'; }
.codicon-dialog-warning:before { content: '\ea6c'; }
.codicon-dialog-info:before { content: '\ea74'; }
.codicon-dialog-close:before { content: '\ea76'; }
.codicon-tree-item-expanded:before { content: '\eab4'; }
.codicon-tree-filter-on-type-on:before { content: '\eb83'; }
.codicon-tree-filter-on-type-off:before { content: '\eb85'; }
.codicon-tree-filter-clear:before { content: '\ea76'; }
.codicon-tree-item-loading:before { content: '\eb19'; }
.codicon-menu-selection:before { content: '\eab2'; }
.codicon-menu-submenu:before { content: '\eab6'; }
.codicon-menubar-more:before { content: '\ea7c'; }
.codicon-scrollbar-button-left:before { content: '\eb6f'; }
.codicon-scrollbar-button-right:before { content: '\eb70'; }
.codicon-scrollbar-button-up:before { content: '\eb71'; }
.codicon-scrollbar-button-down:before { content: '\eb6e'; }
.codicon-toolbar-more:before { content: '\ea7c'; }
.codicon-quick-input-back:before { content: '\ea9b'; }
.codicon-widget-close:before { content: '\ea76'; }
.codicon-goto-previous-location:before { content: '\eaa1'; }
.codicon-goto-next-location:before { content: '\ea9a'; }
.codicon-diff-review-insert:before { content: '\ea60'; }
.codicon-diff-review-remove:before { content: '\eb3b'; }
.codicon-diff-review-close:before { content: '\ea76'; }
.codicon-parameter-hints-next:before { content: '\eab4'; }
.codicon-parameter-hints-previous:before { content: '\eab7'; }
.codicon-suggest-more-info:before { content: '\eab6'; }
.codicon-inline-suggestion-hints-next:before { content: '\eab6'; }
.codicon-inline-suggestion-hints-previous:before { content: '\eab5'; }
.codicon-diff-insert:before { content: '\ea60'; }
.codicon-diff-remove:before { content: '\eb3b'; }
.codicon-find-selection:before { content: '\eb85'; }
.codicon-find-collapsed:before { content: '\eab6'; }
.codicon-find-expanded:before { content: '\eab4'; }
.codicon-find-replace:before { content: '\eb3d'; }
.codicon-find-replace-all:before { content: '\eb3c'; }
.codicon-find-previous-match:before { content: '\eaa1'; }
.codicon-find-next-match:before { content: '\ea9a'; }
.codicon-folding-expanded:before { content: '\eab4'; }
.codicon-folding-collapsed:before { content: '\eab6'; }
.codicon-folding-manual-collapsed:before { content: '\eab6'; }
.codicon-folding-manual-expanded:before { content: '\eab4'; }
.codicon-marker-navigation-next:before { content: '\ea9a'; }
.codicon-marker-navigation-previous:before { content: '\eaa1'; }
.codicon-extensions-warning-message:before { content: '\ea6c'; }
.monaco-editor .inputarea.ime-input { background-color: #f7f7f7; }
.monaco-editor .view-overlays .current-line { border: 2px solid #eeeeee; }
.monaco-editor .margin-view-overlays .current-line-margin { border: 2px solid #eeeeee; }
.monaco-editor .bracket-indent-guide.lvl-0 { --guide-color: rgba(4, 49, 250, 0.3); --guide-color-active: #0431fa; }
.monaco-editor .bracket-indent-guide.lvl-1 { --guide-color: rgba(49, 147, 49, 0.3); --guide-color-active: #319331; }
.monaco-editor .bracket-indent-guide.lvl-2 { --guide-color: rgba(123, 56, 20, 0.3); --guide-color-active: #7b3814; }
.monaco-editor .bracket-indent-guide.lvl-3 { --guide-color: rgba(4, 49, 250, 0.3); --guide-color-active: #0431fa; }
.monaco-editor .bracket-indent-guide.lvl-4 { --guide-color: rgba(49, 147, 49, 0.3); --guide-color-active: #319331; }
.monaco-editor .bracket-indent-guide.lvl-5 { --guide-color: rgba(123, 56, 20, 0.3); --guide-color-active: #7b3814; }
.monaco-editor .bracket-indent-guide.lvl-6 { --guide-color: rgba(4, 49, 250, 0.3); --guide-color-active: #0431fa; }
.monaco-editor .bracket-indent-guide.lvl-7 { --guide-color: rgba(49, 147, 49, 0.3); --guide-color-active: #319331; }
.monaco-editor .bracket-indent-guide.lvl-8 { --guide-color: rgba(123, 56, 20, 0.3); --guide-color-active: #7b3814; }
.monaco-editor .bracket-indent-guide.lvl-9 { --guide-color: rgba(4, 49, 250, 0.3); --guide-color-active: #0431fa; }
.monaco-editor .bracket-indent-guide.lvl-10 { --guide-color: rgba(49, 147, 49, 0.3); --guide-color-active: #319331; }
.monaco-editor .bracket-indent-guide.lvl-11 { --guide-color: rgba(123, 56, 20, 0.3); --guide-color-active: #7b3814; }
.monaco-editor .bracket-indent-guide.lvl-12 { --guide-color: rgba(4, 49, 250, 0.3); --guide-color-active: #0431fa; }
.monaco-editor .bracket-indent-guide.lvl-13 { --guide-color: rgba(49, 147, 49, 0.3); --guide-color-active: #319331; }
.monaco-editor .bracket-indent-guide.lvl-14 { --guide-color: rgba(123, 56, 20, 0.3); --guide-color-active: #7b3814; }
.monaco-editor .bracket-indent-guide.lvl-15 { --guide-color: rgba(4, 49, 250, 0.3); --guide-color-active: #0431fa; }
.monaco-editor .bracket-indent-guide.lvl-16 { --guide-color: rgba(49, 147, 49, 0.3); --guide-color-active: #319331; }
.monaco-editor .bracket-indent-guide.lvl-17 { --guide-color: rgba(123, 56, 20, 0.3); --guide-color-active: #7b3814; }
.monaco-editor .bracket-indent-guide.lvl-18 { --guide-color: rgba(4, 49, 250, 0.3); --guide-color-active: #0431fa; }
.monaco-editor .bracket-indent-guide.lvl-19 { --guide-color: rgba(49, 147, 49, 0.3); --guide-color-active: #319331; }
.monaco-editor .bracket-indent-guide.lvl-20 { --guide-color: rgba(123, 56, 20, 0.3); --guide-color-active: #7b3814; }
.monaco-editor .bracket-indent-guide.lvl-21 { --guide-color: rgba(4, 49, 250, 0.3); --guide-color-active: #0431fa; }
.monaco-editor .bracket-indent-guide.lvl-22 { --guide-color: rgba(49, 147, 49, 0.3); --guide-color-active: #319331; }
.monaco-editor .bracket-indent-guide.lvl-23 { --guide-color: rgba(123, 56, 20, 0.3); --guide-color-active: #7b3814; }
.monaco-editor .bracket-indent-guide.lvl-24 { --guide-color: rgba(4, 49, 250, 0.3); --guide-color-active: #0431fa; }
.monaco-editor .bracket-indent-guide.lvl-25 { --guide-color: rgba(49, 147, 49, 0.3); --guide-color-active: #319331; }
.monaco-editor .bracket-indent-guide.lvl-26 { --guide-color: rgba(123, 56, 20, 0.3); --guide-color-active: #7b3814; }
.monaco-editor .bracket-indent-guide.lvl-27 { --guide-color: rgba(4, 49, 250, 0.3); --guide-color-active: #0431fa; }
.monaco-editor .bracket-indent-guide.lvl-28 { --guide-color: rgba(49, 147, 49, 0.3); --guide-color-active: #319331; }
.monaco-editor .bracket-indent-guide.lvl-29 { --guide-color: rgba(123, 56, 20, 0.3); --guide-color-active: #7b3814; }
.monaco-editor .vertical { box-shadow: 1px 0 0 0 var(--guide-color) inset; }
.monaco-editor .horizontal-top { border-top: 1px solid var(--guide-color); }
.monaco-editor .horizontal-bottom { border-bottom: 1px solid var(--guide-color); }
.monaco-editor .vertical.indent-active { box-shadow: 1px 0 0 0 var(--guide-color-active) inset; }
.monaco-editor .horizontal-top.indent-active { border-top: 1px solid var(--guide-color-active); }
.monaco-editor .horizontal-bottom.indent-active { border-bottom: 1px solid var(--guide-color-active); }
.monaco-editor .line-numbers.dimmed-line-number { color: rgba(153, 153, 153, 0.4); }
.monaco-editor .cursors-layer .cursor { background-color: #000000; border-color: #000000; color: #ffffff; }
.monaco-editor .unexpected-closing-bracket { color: rgba(255, 18, 18, 0.8); }
.monaco-editor .bracket-highlighting-0 { color: #0431fa; }
.monaco-editor .bracket-highlighting-1 { color: #319331; }
.monaco-editor .bracket-highlighting-2 { color: #7b3814; }
.monaco-editor .bracket-highlighting-3 { color: #0431fa; }
.monaco-editor .bracket-highlighting-4 { color: #319331; }
.monaco-editor .bracket-highlighting-5 { color: #7b3814; }
.monaco-editor .bracket-highlighting-6 { color: #0431fa; }
.monaco-editor .bracket-highlighting-7 { color: #319331; }
.monaco-editor .bracket-highlighting-8 { color: #7b3814; }
.monaco-editor .bracket-highlighting-9 { color: #0431fa; }
.monaco-editor .bracket-highlighting-10 { color: #319331; }
.monaco-editor .bracket-highlighting-11 { color: #7b3814; }
.monaco-editor .bracket-highlighting-12 { color: #0431fa; }
.monaco-editor .bracket-highlighting-13 { color: #319331; }
.monaco-editor .bracket-highlighting-14 { color: #7b3814; }
.monaco-editor .bracket-highlighting-15 { color: #0431fa; }
.monaco-editor .bracket-highlighting-16 { color: #319331; }
.monaco-editor .bracket-highlighting-17 { color: #7b3814; }
.monaco-editor .bracket-highlighting-18 { color: #0431fa; }
.monaco-editor .bracket-highlighting-19 { color: #319331; }
.monaco-editor .bracket-highlighting-20 { color: #7b3814; }
.monaco-editor .bracket-highlighting-21 { color: #0431fa; }
.monaco-editor .bracket-highlighting-22 { color: #319331; }
.monaco-editor .bracket-highlighting-23 { color: #7b3814; }
.monaco-editor .bracket-highlighting-24 { color: #0431fa; }
.monaco-editor .bracket-highlighting-25 { color: #319331; }
.monaco-editor .bracket-highlighting-26 { color: #7b3814; }
.monaco-editor .bracket-highlighting-27 { color: #0431fa; }
.monaco-editor .bracket-highlighting-28 { color: #319331; }
.monaco-editor .bracket-highlighting-29 { color: #7b3814; }
.monaco-editor .squiggly-error { background: url("data:image/svg+xml,%3Csvg%20xmlns%3D'http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg'%20viewBox%3D'0%200%206%203'%20enable-background%3D'new%200%200%206%203'%20height%3D'3'%20width%3D'6'%3E%3Cg%20fill%3D'%23e51400'%3E%3Cpolygon%20points%3D'5.5%2C0%202.5%2C3%201.1%2C3%204.1%2C0'%2F%3E%3Cpolygon%20points%3D'4%2C0%206%2C2%206%2C0.6%205.4%2C0'%2F%3E%3Cpolygon%20points%3D'0%2C2%201%2C3%202.4%2C3%200%2C0.6'%2F%3E%3C%2Fg%3E%3C%2Fsvg%3E") repeat-x bottom left; }
.monaco-editor .squiggly-warning { background: url("data:image/svg+xml,%3Csvg%20xmlns%3D'http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg'%20viewBox%3D'0%200%206%203'%20enable-background%3D'new%200%200%206%203'%20height%3D'3'%20width%3D'6'%3E%3Cg%20fill%3D'%23bf8803'%3E%3Cpolygon%20points%3D'5.5%2C0%202.5%2C3%201.1%2C3%204.1%2C0'%2F%3E%3Cpolygon%20points%3D'4%2C0%206%2C2%206%2C0.6%205.4%2C0'%2F%3E%3Cpolygon%20points%3D'0%2C2%201%2C3%202.4%2C3%200%2C0.6'%2F%3E%3C%2Fg%3E%3C%2Fsvg%3E") repeat-x bottom left; }
.monaco-editor .squiggly-info { background: url("data:image/svg+xml,%3Csvg%20xmlns%3D'http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg'%20viewBox%3D'0%200%206%203'%20enable-background%3D'new%200%200%206%203'%20height%3D'3'%20width%3D'6'%3E%3Cg%20fill%3D'%231a85ff'%3E%3Cpolygon%20points%3D'5.5%2C0%202.5%2C3%201.1%2C3%204.1%2C0'%2F%3E%3Cpolygon%20points%3D'4%2C0%206%2C2%206%2C0.6%205.4%2C0'%2F%3E%3Cpolygon%20points%3D'0%2C2%201%2C3%202.4%2C3%200%2C0.6'%2F%3E%3C%2Fg%3E%3C%2Fsvg%3E") repeat-x bottom left; }
.monaco-editor .squiggly-hint { background: url("data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20height%3D%223%22%20width%3D%2212%22%3E%3Cg%20fill%3D%22%236c6c6c%22%3E%3Ccircle%20cx%3D%221%22%20cy%3D%221%22%20r%3D%221%22%2F%3E%3Ccircle%20cx%3D%225%22%20cy%3D%221%22%20r%3D%221%22%2F%3E%3Ccircle%20cx%3D%229%22%20cy%3D%221%22%20r%3D%221%22%2F%3E%3C%2Fg%3E%3C%2Fsvg%3E") no-repeat bottom left; }
.monaco-editor.showUnused .squiggly-inline-unnecessary { opacity: 0.467; }
.monaco-editor .selectionHighlight { background-color: rgba(173, 214, 255, 0.15); }

	.monaco-editor .diagonal-fill {
		background-image: linear-gradient(
			-45deg,
			rgba(34, 34, 34, 0.2) 12.5%,
			#0000 12.5%, #0000 50%,
			rgba(34, 34, 34, 0.2) 50%, rgba(34, 34, 34, 0.2) 62.5%,
			#0000 62.5%, #0000 100%
		);
		background-size: 8px 8px;
	}
	
.monaco-editor .findMatch { background-color: rgba(234, 92, 0, 0.33); }
.monaco-editor .currentFindMatch { background-color: #a8ac94; }
.monaco-editor .findScope { background-color: rgba(180, 180, 180, 0.3); }
.monaco-editor .find-widget { background-color: #f3f3f3; }
.monaco-editor .find-widget { box-shadow: 0 0 8px 2px rgba(0, 0, 0, 0.16); }
.monaco-editor .find-widget { color: #616161; }
.monaco-editor .find-widget.no-results .matchesCount { color: #a1260d; }
.monaco-editor .find-widget .monaco-sash { background-color: #c8c8c8; }

		.monaco-editor .find-widget .button:not(.disabled):hover,
		.monaco-editor .find-widget .codicon-find-selection:hover {
			background-color: rgba(184, 184, 184, 0.31) !important;
		}
	
.monaco-editor .find-widget .monaco-inputbox.synthetic-focus { outline-color: #0090f1; }
.monaco-editor .monaco-hover .hover-row:not(:first-child):not(:empty) { border-top: 1px solid rgba(200, 200, 200, 0.5); }
.monaco-editor .monaco-hover hr { border-top: 1px solid rgba(200, 200, 200, 0.5); }
.monaco-editor .monaco-hover hr { border-bottom: 0px solid rgba(200, 200, 200, 0.5); }
.monaco-editor { --vscode-foreground: #616161;
--vscode-disabledForeground: rgba(97, 97, 97, 0.5);
--vscode-errorForeground: #a1260d;
--vscode-descriptionForeground: #717171;
--vscode-icon-foreground: #424242;
--vscode-focusBorder: #0090f1;
--vscode-textSeparator-foreground: rgba(0, 0, 0, 0.18);
--vscode-textLink-foreground: #006ab1;
--vscode-textLink-activeForeground: #006ab1;
--vscode-textPreformat-foreground: #a31515;
--vscode-textBlockQuote-background: rgba(127, 127, 127, 0.1);
--vscode-textBlockQuote-border: rgba(0, 122, 204, 0.5);
--vscode-textCodeBlock-background: rgba(220, 220, 220, 0.4);
--vscode-widget-shadow: rgba(0, 0, 0, 0.16);
--vscode-input-background: #ffffff;
--vscode-input-foreground: #616161;
--vscode-inputOption-activeBorder: #007acc;
--vscode-inputOption-hoverBackground: rgba(184, 184, 184, 0.31);
--vscode-inputOption-activeBackground: rgba(0, 144, 241, 0.2);
--vscode-inputOption-activeForeground: #000000;
--vscode-input-placeholderForeground: rgba(97, 97, 97, 0.5);
--vscode-inputValidation-infoBackground: #d6ecf2;
--vscode-inputValidation-infoBorder: #007acc;
--vscode-inputValidation-warningBackground: #f6f5d2;
--vscode-inputValidation-warningBorder: #b89500;
--vscode-inputValidation-errorBackground: #f2dede;
--vscode-inputValidation-errorBorder: #be1100;
--vscode-dropdown-background: #ffffff;
--vscode-dropdown-foreground: #616161;
--vscode-dropdown-border: #cecece;
--vscode-button-foreground: #ffffff;
--vscode-button-separator: rgba(255, 255, 255, 0.4);
--vscode-button-background: #007acc;
--vscode-button-hoverBackground: #0062a3;
--vscode-button-secondaryForeground: #ffffff;
--vscode-button-secondaryBackground: #5f6a79;
--vscode-button-secondaryHoverBackground: #4c5561;
--vscode-badge-background: #c4c4c4;
--vscode-badge-foreground: #333333;
--vscode-scrollbar-shadow: #dddddd;
--vscode-scrollbarSlider-background: rgba(100, 100, 100, 0.4);
--vscode-scrollbarSlider-hoverBackground: rgba(100, 100, 100, 0.7);
--vscode-scrollbarSlider-activeBackground: rgba(0, 0, 0, 0.6);
--vscode-progressBar-background: #0e70c0;
--vscode-editorError-foreground: #e51400;
--vscode-editorWarning-foreground: #bf8803;
--vscode-editorInfo-foreground: #1a85ff;
--vscode-editorHint-foreground: #6c6c6c;
--vscode-sash-hoverBorder: #0090f1;
--vscode-editor-background: #f7f7f7;
--vscode-editor-foreground: #000000;
--vscode-editorStickyScroll-background: #f7f7f7;
--vscode-editorStickyScrollHover-background: #f0f0f0;
--vscode-editorWidget-background: #f3f3f3;
--vscode-editorWidget-foreground: #616161;
--vscode-editorWidget-border: #c8c8c8;
--vscode-quickInput-background: #f3f3f3;
--vscode-quickInput-foreground: #616161;
--vscode-quickInputTitle-background: rgba(0, 0, 0, 0.06);
--vscode-pickerGroup-foreground: #0066bf;
--vscode-pickerGroup-border: #cccedb;
--vscode-keybindingLabel-background: rgba(221, 221, 221, 0.4);
--vscode-keybindingLabel-foreground: #555555;
--vscode-keybindingLabel-border: rgba(204, 204, 204, 0.4);
--vscode-keybindingLabel-bottomBorder: rgba(187, 187, 187, 0.4);
--vscode-editor-selectionBackground: #add6ff;
--vscode-editor-inactiveSelectionBackground: #e5ebf1;
--vscode-editor-selectionHighlightBackground: rgba(173, 214, 255, 0.3);
--vscode-editor-findMatchBackground: #a8ac94;
--vscode-editor-findMatchHighlightBackground: rgba(234, 92, 0, 0.33);
--vscode-editor-findRangeHighlightBackground: rgba(180, 180, 180, 0.3);
--vscode-searchEditor-findMatchBackground: rgba(234, 92, 0, 0.22);
--vscode-search-resultsInfoForeground: #616161;
--vscode-editor-hoverHighlightBackground: rgba(173, 214, 255, 0.15);
--vscode-editorHoverWidget-background: #f3f3f3;
--vscode-editorHoverWidget-foreground: #616161;
--vscode-editorHoverWidget-border: #c8c8c8;
--vscode-editorHoverWidget-statusBarBackground: #e7e7e7;
--vscode-editorLink-activeForeground: #0000ff;
--vscode-editorInlayHint-foreground: #616161;
--vscode-editorInlayHint-background: rgba(196, 196, 196, 0.3);
--vscode-editorInlayHint-typeForeground: #616161;
--vscode-editorInlayHint-typeBackground: rgba(196, 196, 196, 0.3);
--vscode-editorInlayHint-parameterForeground: #616161;
--vscode-editorInlayHint-parameterBackground: rgba(196, 196, 196, 0.3);
--vscode-editorLightBulb-foreground: #ddb100;
--vscode-editorLightBulbAutoFix-foreground: #007acc;
--vscode-diffEditor-insertedTextBackground: rgba(155, 185, 85, 0.09);
--vscode-diffEditor-removedTextBackground: rgba(255, 0, 0, 0.03);
--vscode-diffEditor-insertedLineBackground: rgba(155, 185, 85, 0.09);
--vscode-diffEditor-removedLineBackground: rgba(255, 0, 0, 0.03);
--vscode-diffEditor-diagonalFill: rgba(34, 34, 34, 0.2);
--vscode-diffEditor-unchangedRegionBackground: #e4e4e4;
--vscode-diffEditor-unchangedRegionForeground: #4d4c4c;
--vscode-diffEditor-unchangedCodeBackground: rgba(184, 184, 184, 0.16);
--vscode-list-focusOutline: #0090f1;
--vscode-list-activeSelectionBackground: #d6ebff;
--vscode-list-activeSelectionForeground: #000000;
--vscode-list-inactiveSelectionBackground: #e4e6f1;
--vscode-list-hoverBackground: #f0f0f0;
--vscode-list-dropBackground: #d6ebff;
--vscode-list-highlightForeground: #0066bf;
--vscode-list-focusHighlightForeground: #0066bf;
--vscode-list-invalidItemForeground: #b89500;
--vscode-list-errorForeground: #b01011;
--vscode-list-warningForeground: #855f00;
--vscode-listFilterWidget-background: #f3f3f3;
--vscode-listFilterWidget-outline: rgba(0, 0, 0, 0);
--vscode-listFilterWidget-noMatchesOutline: #be1100;
--vscode-listFilterWidget-shadow: rgba(0, 0, 0, 0.16);
--vscode-list-filterMatchBackground: rgba(234, 92, 0, 0.33);
--vscode-tree-indentGuidesStroke: #a9a9a9;
--vscode-tree-inactiveIndentGuidesStroke: rgba(169, 169, 169, 0.4);
--vscode-tree-tableColumnsBorder: rgba(97, 97, 97, 0.13);
--vscode-tree-tableOddRowsBackground: rgba(97, 97, 97, 0.04);
--vscode-list-deemphasizedForeground: #8e8e90;
--vscode-checkbox-background: #ffffff;
--vscode-checkbox-selectBackground: #f3f3f3;
--vscode-checkbox-foreground: #616161;
--vscode-checkbox-border: #cecece;
--vscode-checkbox-selectBorder: #424242;
--vscode-quickInputList-focusForeground: #000000;
--vscode-quickInputList-focusBackground: #d6ebff;
--vscode-menu-foreground: #616161;
--vscode-menu-background: #ffffff;
--vscode-menu-selectionForeground: #000000;
--vscode-menu-selectionBackground: #d6ebff;
--vscode-menu-separatorBackground: #d4d4d4;
--vscode-toolbar-hoverBackground: rgba(184, 184, 184, 0.31);
--vscode-toolbar-activeBackground: rgba(166, 166, 166, 0.31);
--vscode-editor-snippetTabstopHighlightBackground: rgba(10, 50, 100, 0.2);
--vscode-editor-snippetFinalTabstopHighlightBorder: rgba(10, 50, 100, 0.5);
--vscode-breadcrumb-foreground: rgba(97, 97, 97, 0.8);
--vscode-breadcrumb-background: #f7f7f7;
--vscode-breadcrumb-focusForeground: #4e4e4e;
--vscode-breadcrumb-activeSelectionForeground: #4e4e4e;
--vscode-breadcrumbPicker-background: #f3f3f3;
--vscode-merge-currentHeaderBackground: rgba(64, 200, 174, 0.5);
--vscode-merge-currentContentBackground: rgba(64, 200, 174, 0.2);
--vscode-merge-incomingHeaderBackground: rgba(64, 166, 255, 0.5);
--vscode-merge-incomingContentBackground: rgba(64, 166, 255, 0.2);
--vscode-merge-commonHeaderBackground: rgba(96, 96, 96, 0.4);
--vscode-merge-commonContentBackground: rgba(96, 96, 96, 0.16);
--vscode-editorOverviewRuler-currentContentForeground: rgba(64, 200, 174, 0.5);
--vscode-editorOverviewRuler-incomingContentForeground: rgba(64, 166, 255, 0.5);
--vscode-editorOverviewRuler-commonContentForeground: rgba(96, 96, 96, 0.4);
--vscode-editorOverviewRuler-findMatchForeground: rgba(209, 134, 22, 0.49);
--vscode-editorOverviewRuler-selectionHighlightForeground: rgba(0, 0, 0, 0);
--vscode-minimap-findMatchHighlight: #d18616;
--vscode-minimap-selectionOccurrenceHighlight: #c9c9c9;
--vscode-minimap-selectionHighlight: #add6ff;
--vscode-minimap-errorHighlight: rgba(255, 18, 18, 0.7);
--vscode-minimap-warningHighlight: #bf8803;
--vscode-minimap-foregroundOpacity: #000000;
--vscode-minimapSlider-background: rgba(100, 100, 100, 0.2);
--vscode-minimapSlider-hoverBackground: rgba(100, 100, 100, 0.35);
--vscode-minimapSlider-activeBackground: rgba(0, 0, 0, 0.3);
--vscode-problemsErrorIcon-foreground: #e51400;
--vscode-problemsWarningIcon-foreground: #bf8803;
--vscode-problemsInfoIcon-foreground: #1a85ff;
--vscode-charts-foreground: #616161;
--vscode-charts-lines: rgba(97, 97, 97, 0.5);
--vscode-charts-red: #e51400;
--vscode-charts-blue: #1a85ff;
--vscode-charts-yellow: #bf8803;
--vscode-charts-orange: #d18616;
--vscode-charts-green: #388a34;
--vscode-charts-purple: #652d90;
--vscode-symbolIcon-arrayForeground: #616161;
--vscode-symbolIcon-booleanForeground: #616161;
--vscode-symbolIcon-classForeground: #d67e00;
--vscode-symbolIcon-colorForeground: #616161;
--vscode-symbolIcon-constantForeground: #616161;
--vscode-symbolIcon-constructorForeground: #652d90;
--vscode-symbolIcon-enumeratorForeground: #d67e00;
--vscode-symbolIcon-enumeratorMemberForeground: #007acc;
--vscode-symbolIcon-eventForeground: #d67e00;
--vscode-symbolIcon-fieldForeground: #007acc;
--vscode-symbolIcon-fileForeground: #616161;
--vscode-symbolIcon-folderForeground: #616161;
--vscode-symbolIcon-functionForeground: #652d90;
--vscode-symbolIcon-interfaceForeground: #007acc;
--vscode-symbolIcon-keyForeground: #616161;
--vscode-symbolIcon-keywordForeground: #616161;
--vscode-symbolIcon-methodForeground: #652d90;
--vscode-symbolIcon-moduleForeground: #616161;
--vscode-symbolIcon-namespaceForeground: #616161;
--vscode-symbolIcon-nullForeground: #616161;
--vscode-symbolIcon-numberForeground: #616161;
--vscode-symbolIcon-objectForeground: #616161;
--vscode-symbolIcon-operatorForeground: #616161;
--vscode-symbolIcon-packageForeground: #616161;
--vscode-symbolIcon-propertyForeground: #616161;
--vscode-symbolIcon-referenceForeground: #616161;
--vscode-symbolIcon-snippetForeground: #616161;
--vscode-symbolIcon-stringForeground: #616161;
--vscode-symbolIcon-structForeground: #616161;
--vscode-symbolIcon-textForeground: #616161;
--vscode-symbolIcon-typeParameterForeground: #616161;
--vscode-symbolIcon-unitForeground: #616161;
--vscode-symbolIcon-variableForeground: #007acc;
--vscode-editor-lineHighlightBorder: #eeeeee;
--vscode-editor-rangeHighlightBackground: rgba(253, 255, 0, 0.2);
--vscode-editor-symbolHighlightBackground: rgba(234, 92, 0, 0.33);
--vscode-editorCursor-foreground: #000000;
--vscode-editorWhitespace-foreground: rgba(51, 51, 51, 0.2);
--vscode-editorIndentGuide-background: #d3d3d3;
--vscode-editorIndentGuide-activeBackground: #939393;
--vscode-editorLineNumber-foreground: #999999;
--vscode-editorActiveLineNumber-foreground: #0b216f;
--vscode-editorLineNumber-activeForeground: #0b216f;
--vscode-editorRuler-foreground: #d3d3d3;
--vscode-editorCodeLens-foreground: #919191;
--vscode-editorBracketMatch-background: rgba(0, 100, 0, 0.1);
--vscode-editorBracketMatch-border: #b9b9b9;
--vscode-editorOverviewRuler-border: rgba(127, 127, 127, 0.3);
--vscode-editorGutter-background: #f7f7f7;
--vscode-editorUnnecessaryCode-opacity: rgba(0, 0, 0, 0.47);
--vscode-editorGhostText-foreground: rgba(0, 0, 0, 0.47);
--vscode-editorOverviewRuler-rangeHighlightForeground: rgba(0, 122, 204, 0.6);
--vscode-editorOverviewRuler-errorForeground: rgba(255, 18, 18, 0.7);
--vscode-editorOverviewRuler-warningForeground: #bf8803;
--vscode-editorOverviewRuler-infoForeground: #1a85ff;
--vscode-editorBracketHighlight-foreground1: #0431fa;
--vscode-editorBracketHighlight-foreground2: #319331;
--vscode-editorBracketHighlight-foreground3: #7b3814;
--vscode-editorBracketHighlight-foreground4: rgba(0, 0, 0, 0);
--vscode-editorBracketHighlight-foreground5: rgba(0, 0, 0, 0);
--vscode-editorBracketHighlight-foreground6: rgba(0, 0, 0, 0);
--vscode-editorBracketHighlight-unexpectedBracket-foreground: rgba(255, 18, 18, 0.8);
--vscode-editorBracketPairGuide-background1: rgba(0, 0, 0, 0);
--vscode-editorBracketPairGuide-background2: rgba(0, 0, 0, 0);
--vscode-editorBracketPairGuide-background3: rgba(0, 0, 0, 0);
--vscode-editorBracketPairGuide-background4: rgba(0, 0, 0, 0);
--vscode-editorBracketPairGuide-background5: rgba(0, 0, 0, 0);
--vscode-editorBracketPairGuide-background6: rgba(0, 0, 0, 0);
--vscode-editorBracketPairGuide-activeBackground1: rgba(0, 0, 0, 0);
--vscode-editorBracketPairGuide-activeBackground2: rgba(0, 0, 0, 0);
--vscode-editorBracketPairGuide-activeBackground3: rgba(0, 0, 0, 0);
--vscode-editorBracketPairGuide-activeBackground4: rgba(0, 0, 0, 0);
--vscode-editorBracketPairGuide-activeBackground5: rgba(0, 0, 0, 0);
--vscode-editorBracketPairGuide-activeBackground6: rgba(0, 0, 0, 0);
--vscode-editorUnicodeHighlight-border: #cea33d;
--vscode-editorUnicodeHighlight-background: rgba(206, 163, 61, 0.08);
--vscode-editorOverviewRuler-bracketMatchForeground: #a0a0a0;
--vscode-editor-linkedEditingBackground: rgba(255, 0, 0, 0.3);
--vscode-editor-wordHighlightBackground: rgba(87, 87, 87, 0.25);
--vscode-editor-wordHighlightStrongBackground: #d6ebff;
--vscode-editor-wordHighlightTextBackground: rgba(173, 214, 255, 0.45);
--vscode-editorOverviewRuler-wordHighlightForeground: rgba(160, 160, 160, 0.8);
--vscode-editorOverviewRuler-wordHighlightStrongForeground: rgba(192, 160, 192, 0.8);
--vscode-editorOverviewRuler-wordHighlightTextForeground: rgba(0, 0, 0, 0);
--vscode-peekViewTitle-background: #f3f3f3;
--vscode-peekViewTitleLabel-foreground: #000000;
--vscode-peekViewTitleDescription-foreground: #616161;
--vscode-peekView-border: #1a85ff;
--vscode-peekViewResult-background: #f3f3f3;
--vscode-peekViewResult-lineForeground: #646465;
--vscode-peekViewResult-fileForeground: #1e1e1e;
--vscode-peekViewResult-selectionBackground: rgba(51, 153, 255, 0.2);
--vscode-peekViewResult-selectionForeground: #6c6c6c;
--vscode-peekViewEditor-background: #f2f8fc;
--vscode-peekViewEditorGutter-background: #f2f8fc;
--vscode-peekViewEditorStickyScroll-background: #f2f8fc;
--vscode-peekViewResult-matchHighlightBackground: rgba(234, 92, 0, 0.3);
--vscode-peekViewEditor-matchHighlightBackground: rgba(245, 216, 2, 0.87);
--vscode-editorMarkerNavigationError-background: #e51400;
--vscode-editorMarkerNavigationError-headerBackground: rgba(229, 20, 0, 0.1);
--vscode-editorMarkerNavigationWarning-background: #bf8803;
--vscode-editorMarkerNavigationWarning-headerBackground: rgba(191, 136, 3, 0.1);
--vscode-editorMarkerNavigationInfo-background: #1a85ff;
--vscode-editorMarkerNavigationInfo-headerBackground: rgba(26, 133, 255, 0.1);
--vscode-editorMarkerNavigation-background: #f7f7f7;
--vscode-editorHoverWidget-highlightForeground: #0066bf;
--vscode-editorSuggestWidget-background: #f3f3f3;
--vscode-editorSuggestWidget-border: #c8c8c8;
--vscode-editorSuggestWidget-foreground: #000000;
--vscode-editorSuggestWidget-selectedForeground: #000000;
--vscode-editorSuggestWidget-selectedBackground: #d6ebff;
--vscode-editorSuggestWidget-highlightForeground: #0066bf;
--vscode-editorSuggestWidget-focusHighlightForeground: #0066bf;
--vscode-editorSuggestWidgetStatus-foreground: rgba(0, 0, 0, 0.5);
--vscode-editor-foldBackground: rgba(173, 214, 255, 0.3);
--vscode-editorGutter-foldingControlForeground: #424242; }

.mtk1 { color: #000000; }
.mtk2 { color: #f7f7f7; }
.mtk3 { color: #808080; }
.mtk4 { color: #ff0000; }
.mtk5 { color: #0451a5; }
.mtk6 { color: #0000ff; }
.mtk7 { color: #098658; }
.mtk8 { color: #008000; }
.mtk9 { color: #dd0000; }
.mtk10 { color: #811f3f; }
.mtk11 { color: #e00000; }
.mtk12 { color: #116644; }
.mtk13 { color: #383838; }
.mtk14 { color: #257693; }
.mtk15 { color: #795e26; }
.mtk16 { color: #001080; }
.mtk17 { color: #cd3131; }
.mtk18 { color: #863b00; }
.mtk19 { color: #af00db; }
.mtk20 { color: #c43b3b; }
.mtk21 { color: #800000; }
.mtk22 { color: #3030c0; }
.mtk23 { color: #666666; }
.mtk24 { color: #778899; }
.mtk25 { color: #c700c7; }
.mtk26 { color: #a31515; }
.mtk27 { color: #4f76ac; }
.mtk28 { color: #008080; }
.mtk29 { color: #001188; }
.mtk30 { color: #4864aa; }
.mtki { font-style: italic; }
.mtkb { font-weight: bold; }
.mtku { text-decoration: underline; text-underline-position: under; }
.mtks { text-decoration: line-through; }
.mtks.mtku { text-decoration: underline line-through; text-underline-position: under; }</style><style type="text/css">.MathJax_Display {text-align: center; margin: 0; position: relative; display: block!important; text-indent: 0; max-width: none; max-height: none; min-width: 0; min-height: 0; width: 100%}
.MathJax .merror {background-color: #FFFF88; color: #CC0000; border: 1px solid #CC0000; padding: 1px 3px; font-style: normal; font-size: 90%}
.MathJax .MJX-monospace {font-family: monospace}
.MathJax .MJX-sans-serif {font-family: sans-serif}
#MathJax_Tooltip {background-color: InfoBackground; color: InfoText; border: 1px solid black; box-shadow: 2px 2px 5px #AAAAAA; -webkit-box-shadow: 2px 2px 5px #AAAAAA; -moz-box-shadow: 2px 2px 5px #AAAAAA; -khtml-box-shadow: 2px 2px 5px #AAAAAA; filter: progid:DXImageTransform.Microsoft.dropshadow(OffX=2, OffY=2, Color='gray', Positive='true'); padding: 3px 4px; z-index: 401; position: absolute; left: 0; top: 0; width: auto; height: auto; display: none}
.MathJax {display: inline; font-style: normal; font-weight: normal; line-height: normal; font-size: 100%; font-size-adjust: none; text-indent: 0; text-align: left; text-transform: none; letter-spacing: normal; word-spacing: normal; word-wrap: normal; white-space: nowrap; float: none; direction: ltr; max-width: none; max-height: none; min-width: 0; min-height: 0; border: 0; padding: 0; margin: 0}
.MathJax:focus, body :focus .MathJax {display: inline-table}
.MathJax.MathJax_FullWidth {text-align: center; display: table-cell!important; width: 10000em!important}
.MathJax img, .MathJax nobr, .MathJax a {border: 0; padding: 0; margin: 0; max-width: none; max-height: none; min-width: 0; min-height: 0; vertical-align: 0; line-height: normal; text-decoration: none}
img.MathJax_strut {border: 0!important; padding: 0!important; margin: 0!important; vertical-align: 0!important}
.MathJax span {display: inline; position: static; border: 0; padding: 0; margin: 0; vertical-align: 0; line-height: normal; text-decoration: none; box-sizing: content-box}
.MathJax nobr {white-space: nowrap!important}
.MathJax img {display: inline!important; float: none!important}
.MathJax * {transition: none; -webkit-transition: none; -moz-transition: none; -ms-transition: none; -o-transition: none}
.MathJax_Processing {visibility: hidden; position: fixed; width: 0; height: 0; overflow: hidden}
.MathJax_Processed {display: none!important}
.MathJax_test {font-style: normal; font-weight: normal; font-size: 100%; font-size-adjust: none; text-indent: 0; text-transform: none; letter-spacing: normal; word-spacing: normal; overflow: hidden; height: 1px}
.MathJax_test.mjx-test-display {display: table!important}
.MathJax_test.mjx-test-inline {display: inline!important; margin-right: -1px}
.MathJax_test.mjx-test-default {display: block!important; clear: both}
.MathJax_ex_box {display: inline-block!important; position: absolute; overflow: hidden; min-height: 0; max-height: none; padding: 0; border: 0; margin: 0; width: 1px; height: 60ex}
.MathJax_em_box {display: inline-block!important; position: absolute; overflow: hidden; min-height: 0; max-height: none; padding: 0; border: 0; margin: 0; width: 1px; height: 60em}
.mjx-test-inline .MathJax_left_box {display: inline-block; width: 0; float: left}
.mjx-test-inline .MathJax_right_box {display: inline-block; width: 0; float: right}
.mjx-test-display .MathJax_right_box {display: table-cell!important; width: 10000em!important; min-width: 0; max-width: none; padding: 0; border: 0; margin: 0}
.MathJax .MathJax_HitBox {cursor: text; background: white; opacity: 0; filter: alpha(opacity=0)}
.MathJax .MathJax_HitBox * {filter: none; opacity: 1; background: transparent}
#MathJax_Tooltip * {filter: none; opacity: 1; background: transparent}
@font-face {font-family: MathJax_Main; src: url('https://colab.research.google.com/static/mathjax/fonts/HTML-CSS/TeX/woff/MathJax_Main-Regular.woff?V=2.7.5') format('woff'), url('https://colab.research.google.com/static/mathjax/fonts/HTML-CSS/TeX/otf/MathJax_Main-Regular.otf?V=2.7.5') format('opentype')}
@font-face {font-family: MathJax_Main-bold; src: url('https://colab.research.google.com/static/mathjax/fonts/HTML-CSS/TeX/woff/MathJax_Main-Bold.woff?V=2.7.5') format('woff'), url('https://colab.research.google.com/static/mathjax/fonts/HTML-CSS/TeX/otf/MathJax_Main-Bold.otf?V=2.7.5') format('opentype')}
@font-face {font-family: MathJax_Main-italic; src: url('https://colab.research.google.com/static/mathjax/fonts/HTML-CSS/TeX/woff/MathJax_Main-Italic.woff?V=2.7.5') format('woff'), url('https://colab.research.google.com/static/mathjax/fonts/HTML-CSS/TeX/otf/MathJax_Main-Italic.otf?V=2.7.5') format('opentype')}
@font-face {font-family: MathJax_Math-italic; src: url('https://colab.research.google.com/static/mathjax/fonts/HTML-CSS/TeX/woff/MathJax_Math-Italic.woff?V=2.7.5') format('woff'), url('https://colab.research.google.com/static/mathjax/fonts/HTML-CSS/TeX/otf/MathJax_Math-Italic.otf?V=2.7.5') format('opentype')}
@font-face {font-family: MathJax_Caligraphic; src: url('https://colab.research.google.com/static/mathjax/fonts/HTML-CSS/TeX/woff/MathJax_Caligraphic-Regular.woff?V=2.7.5') format('woff'), url('https://colab.research.google.com/static/mathjax/fonts/HTML-CSS/TeX/otf/MathJax_Caligraphic-Regular.otf?V=2.7.5') format('opentype')}
@font-face {font-family: MathJax_Size1; src: url('https://colab.research.google.com/static/mathjax/fonts/HTML-CSS/TeX/woff/MathJax_Size1-Regular.woff?V=2.7.5') format('woff'), url('https://colab.research.google.com/static/mathjax/fonts/HTML-CSS/TeX/otf/MathJax_Size1-Regular.otf?V=2.7.5') format('opentype')}
@font-face {font-family: MathJax_Size2; src: url('https://colab.research.google.com/static/mathjax/fonts/HTML-CSS/TeX/woff/MathJax_Size2-Regular.woff?V=2.7.5') format('woff'), url('https://colab.research.google.com/static/mathjax/fonts/HTML-CSS/TeX/otf/MathJax_Size2-Regular.otf?V=2.7.5') format('opentype')}
@font-face {font-family: MathJax_Size3; src: url('https://colab.research.google.com/static/mathjax/fonts/HTML-CSS/TeX/woff/MathJax_Size3-Regular.woff?V=2.7.5') format('woff'), url('https://colab.research.google.com/static/mathjax/fonts/HTML-CSS/TeX/otf/MathJax_Size3-Regular.otf?V=2.7.5') format('opentype')}
@font-face {font-family: MathJax_Size4; src: url('https://colab.research.google.com/static/mathjax/fonts/HTML-CSS/TeX/woff/MathJax_Size4-Regular.woff?V=2.7.5') format('woff'), url('https://colab.research.google.com/static/mathjax/fonts/HTML-CSS/TeX/otf/MathJax_Size4-Regular.otf?V=2.7.5') format('opentype')}
.MathJax .noError {vertical-align: ; font-size: 90%; text-align: left; color: black; padding: 1px 3px; border: 1px solid}
</style><link type="text/css" rel="stylesheet" href="./Task 1 - Chatbot with Rule-based responses_files/css2(1)"></head><body class="" style="overscroll-behavior: contain;"><div style="visibility: hidden; overflow: hidden; position: absolute; top: 0px; height: 1px; width: auto; padding: 0px; border: 0px; margin: 0px; text-align: left; text-indent: 0px; text-transform: none; line-height: normal; letter-spacing: normal; word-spacing: normal;"><div id="MathJax_Hidden"></div></div><div id="MathJax_Message" style="display: none;"></div><div class="scripts"><script nonce="">window.performance.mark('external_scripts_start');</script><script src="./Task 1 - Chatbot with Rule-based responses_files/gapi_loader.js.download" nonce=""></script><script src="./Task 1 - Chatbot with Rule-based responses_files/socketio_binary.js.download" nonce=""></script><script src="./Task 1 - Chatbot with Rule-based responses_files/analytics_binary.js.download" nonce=""></script><script src="./Task 1 - Chatbot with Rule-based responses_files/MathJax.js.download" nonce=""></script><script src="./Task 1 - Chatbot with Rule-based responses_files/js_monaco_editor_vs_loader.js.download" nonce=""></script><script nonce="">window.performance.mark('external_scripts_end'); window.performance.measure('external_scripts', 'external_scripts_start', 'external_scripts_end'); window.performance.mark('colab_load_start');</script><script src="./Task 1 - Chatbot with Rule-based responses_files/external_binary.js.download" nonce=""></script><script nonce="">
          window.performance.mark('colab_load_end');
          window.performance.measure('colab_load', 'colab_load_start', 'colab_load_end');
        </script></div><colab-snackbar leading="" labeltext="" id="message-area" class="message-area"><template shadowrootmode="open"><!----><style>
        :host .mdc-snackbar__surface {
          background-color: var(--colab-snackbar-surface-color);
        }
      </style>
      <!--?lit$571398431$-->
      <div class="mdc-snackbar  mdc-snackbar--leading ">
        <div class="mdc-snackbar__surface">
          <!--?lit$571398431$-->
          <div class="mdc-snackbar__actions">
            <slot name="action"></slot>
            <slot name="dismiss"></slot>
          </div>
        </div>
      </div><!--?--></template>
      <md-icon-button class="close" slot="dismiss" title="Close" data-aria-label="Close" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Close">
        <!--?lit$571398431$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$571398431$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$571398431$--><span class="icon"><slot></slot></span>
        <!--?lit$571398431$-->
        <!--?lit$571398431$--><span class="touch"></span>
        <!--?lit$571398431$-->
  </button></template>
        <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>close</md-icon>
      </md-icon-button>
    </colab-snackbar><colab-snackbar leading="" labeltext="" id="message-area-secondary" class="message-area"><template shadowrootmode="open"><!----><style>
        :host .mdc-snackbar__surface {
          background-color: var(--colab-snackbar-surface-color);
        }
      </style>
      <!--?lit$571398431$-->
      <div class="mdc-snackbar mdc-snackbar--leading">
        <div class="mdc-snackbar__surface">
          <!--?lit$571398431$-->
          <div class="mdc-snackbar__actions">
            <slot name="action"></slot>
            <slot name="dismiss"></slot>
          </div>
        </div>
      </div><!--?--></template>
      <md-icon-button class="close" slot="dismiss" title="Close" data-aria-label="Close" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Close">
        <!--?lit$571398431$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$571398431$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$571398431$--><span class="icon"><slot></slot></span>
        <!--?lit$571398431$-->
        <!--?lit$571398431$--><span class="touch"></span>
        <!--?lit$571398431$-->
  </button></template>
        <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>close</md-icon>
      </md-icon-button>
    </colab-snackbar><div ng-non-bindable=""></div><div class="gb_r" ng-non-bindable=""><div class="gb_wc"><div>Google Account</div><div class="gb_wb">Nithish</div><div>indlanithish2002@gmail.com</div></div></div><script nonce="">this.gbar_=this.gbar_||{};(function(_){var window=this;
try{
var zd;_.yd=function(a){var b=typeof a;return b=="object"&&a!=null||b=="function"};zd=class extends _.id{};_.Ad=function(a,b){if(b in a.i)return a.i[b];throw new zd;};_.Bd=function(a){return _.Ad(_.fd.i(),a)};
}catch(e){_._DumpException(e)}
try{
/*

 SPDX-License-Identifier: Apache-2.0
*/
var Hd,Rd,Td;_.Cd=function(a){if(a==null)return a;if(typeof a==="string"){if(!a)return;a=+a}if(typeof a==="number")return Number.isFinite(a)?a|0:void 0};_.Dd=function(a){const b=a.length;if(b>0){const c=Array(b);for(let d=0;d<b;d++)c[d]=a[d];return c}return[]};_.Fd=function(a){if(a instanceof _.Ed)return a.i;throw Error("E");};Hd=function(a){return new Gd(b=>b.substr(0,a.length+1).toLowerCase()===a+":")};
_.Jd=function(a,b=_.Id){if(a instanceof _.Ed)return a;for(let c=0;c<b.length;++c){const d=b[c];if(d instanceof Gd&&d.Xg(a))return new _.Ed(a)}};_.Ld=function(a){if(Kd.test(a))return a};_.Md=function(a){return a instanceof _.Ed?_.Fd(a):_.Ld(a)};_.Nd=function(a,b){var c=Array.prototype.slice.call(arguments,1);return function(){var d=c.slice();d.push.apply(d,arguments);return a.apply(this,d)}};_.Od=function(a,b,c){return _.tb(a,b,c,!1)!==void 0};_.Pd=function(a,b){return _.Cd(_.Cc(a,b))};
_.S=function(a,b){a=_.Cc(a,b);return a==null?a:Number.isFinite(a)?a|0:void 0};_.T=function(a,b,c=0){return _.ub(_.Pd(a,b),c)};_.Qd=function(a,b,c=0){return _.ub(_.S(a,b),c)};Rd=0;_.Sd=function(a){return Object.prototype.hasOwnProperty.call(a,_.Jb)&&a[_.Jb]||(a[_.Jb]=++Rd)};Td=function(a){return a};_.Ud=function(a){var b=null,c=_.t.trustedTypes;if(!c||!c.createPolicy)return b;try{b=c.createPolicy(a,{createHTML:Td,createScript:Td,createScriptURL:Td})}catch(d){_.t.console&&_.t.console.error(d.message)}return b};
_.Vd=function(a,b){return a.lastIndexOf(b,0)==0};_.Wd=function(a,b){return Array.prototype.some.call(a,b,void 0)};try{(new self.OffscreenCanvas(0,0)).getContext("2d")}catch(a){};var Xd;_.Yd=function(){Xd===void 0&&(Xd=_.Ud("ogb-qtm#html"));return Xd};var ae;_.Zd=class{constructor(a){this.i=a}toString(){return this.i+""}};_.$d=function(a){return a instanceof _.Zd&&a.constructor===_.Zd?a.i:"type_error:TrustedResourceUrl"};ae={};_.be=function(a){const b=_.Yd();a=b?b.createScriptURL(a):a;return new _.Zd(a,ae)};_.Ed=class{constructor(a){this.i=a}toString(){return this.i}};_.ce=new _.Ed("about:invalid#zClosurez");var Gd,Kd;Gd=class{constructor(a){this.Xg=a}};_.Id=[Hd("data"),Hd("http"),Hd("https"),Hd("mailto"),Hd("ftp"),new Gd(a=>/^[^:]*([/?#]|$)/.test(a))];Kd=/^\s*(?!javascript:)(?:[\w+.-]+:|[^:/?#]*(?:[/?#]|$))/i;_.de={};_.ee=class{constructor(a){this.i=a}toString(){return this.i.toString()}};_.fe=new _.ee("",_.de);_.ge=RegExp("^[-+,.\"'%_!#/ a-zA-Z0-9\\[\\]]+$");_.he=RegExp("\\b(url\\([ \t\n]*)('[ -&(-\\[\\]-~]*'|\"[ !#-\\[\\]-~]*\"|[!#-&*-\\[\\]-~]*)([ \t\n]*\\))","g");_.ie=RegExp("\\b(calc|cubic-bezier|fit-content|hsl|hsla|linear-gradient|matrix|minmax|radial-gradient|repeat|rgb|rgba|(rotate|scale|translate)(X|Y|Z|3d)?|steps|var)\\([-+*/0-9a-zA-Z.%#\\[\\], ]+\\)","g");_.je={};_.le=function(a){return a instanceof _.ke&&a.constructor===_.ke?a.i:"type_error:SafeHtml"};_.ke=class{constructor(a){this.i=a}toString(){return this.i.toString()}};_.me=new _.ke(_.t.trustedTypes&&_.t.trustedTypes.emptyHTML||"",_.je);var oe;_.ne=function(a){let b=!1,c;return function(){b||(c=a(),b=!0);return c}}(function(){var a=document.createElement("div"),b=document.createElement("div");b.appendChild(document.createElement("div"));a.appendChild(b);b=a.firstChild.firstChild;a.innerHTML=_.le(_.me);return!b.parentElement});oe=/^[\w+/_-]+[=]{0,2}$/;
_.pe=function(a){a=(a||_.t).document;return a.querySelector?(a=a.querySelector('style[nonce],link[rel="stylesheet"][nonce]'))&&(a=a.nonce||a.getAttribute("nonce"))&&oe.test(a)?a:"":""};_.qe=function(a,b){this.width=a;this.height=b};_.n=_.qe.prototype;_.n.aspectRatio=function(){return this.width/this.height};_.n.Fb=function(){return!(this.width*this.height)};_.n.ceil=function(){this.width=Math.ceil(this.width);this.height=Math.ceil(this.height);return this};_.n.floor=function(){this.width=Math.floor(this.width);this.height=Math.floor(this.height);return this};_.n.round=function(){this.width=Math.round(this.width);this.height=Math.round(this.height);return this};_.U=function(a,b){var c=b||document;if(c.getElementsByClassName)a=c.getElementsByClassName(a)[0];else{c=document;var d=b||c;a=d.querySelectorAll&&d.querySelector&&a?d.querySelector(a?"."+a:""):_.re(c,a,b)[0]||null}return a||null};
_.re=function(a,b,c){var d;a=c||a;if(a.querySelectorAll&&a.querySelector&&b)return a.querySelectorAll(b?"."+b:"");if(b&&a.getElementsByClassName){var e=a.getElementsByClassName(b);return e}e=a.getElementsByTagName("*");if(b){var f={};for(c=d=0;a=e[c];c++){var g=a.className;typeof g.split=="function"&&_.sa(g.split(/\s+/),b)&&(f[d++]=a)}f.length=d;return f}return e};_.te=function(a){return _.se(document,a)};
_.se=function(a,b){b=String(b);a.contentType==="application/xhtml+xml"&&(b=b.toLowerCase());return a.createElement(b)};_.ue=function(a){for(var b;b=a.firstChild;)a.removeChild(b)};_.ve=function(a){return a.nodeType==9?a:a.ownerDocument||a.document};
}catch(e){_._DumpException(e)}
try{
_.Zi=function(a){var b;let c;const d=(c=(b=(a.ownerDocument&&a.ownerDocument.defaultView||window).document).querySelector)==null?void 0:c.call(b,"script[nonce]");(b=d?d.nonce||d.getAttribute("nonce")||"":"")&&a.setAttribute("nonce",b)};_.$i=function(a){if(!a)return null;a=_.J(a,4);var b;a===null||a===void 0?b=null:b=_.be(a);return b};_.aj=class extends _.Q{constructor(a){super(a)}};_.bj=function(a,b){return(b||document).getElementsByTagName(String(a))};
}catch(e){_._DumpException(e)}
try{
var dj=function(a,b,c){a<b?cj(a+1,b):_.Oc.log(Error("da`"+a+"`"+b),{url:c})},cj=function(a,b){if(ej){const c=_.te("SCRIPT");c.async=!0;c.type="text/javascript";c.charset="UTF-8";c.src=_.$d(ej);_.Zi(c);c.onerror=_.Nd(dj,a,b,c.src);_.bj("HEAD")[0].appendChild(c)}},fj=class extends _.Q{constructor(a){super(a)}};var gj=_.F(_.$c,fj,17)||new fj,hj,ej=(hj=_.F(gj,_.aj,1))?_.$i(hj):null,ij,jj=(ij=_.F(gj,_.aj,2))?_.$i(ij):null,kj=function(){cj(1,2);if(jj){const b=_.te("LINK");b.setAttribute("type","text/css");b.rel="stylesheet";b.href=_.$d(jj).toString();var a=_.pe(b.ownerDocument&&b.ownerDocument.defaultView);a&&b.setAttribute("nonce",a);(a=_.pe())&&b.setAttribute("nonce",a);_.bj("HEAD")[0].appendChild(b)}};(function(){const a=_.ad();if(_.I(a,18))kj();else{const b=_.Pd(a,19)||0;window.addEventListener("load",()=>{window.setTimeout(kj,b)})}})();
}catch(e){_._DumpException(e)}
})(this.gbar_);
// Google Inc.
</script><div id="loom-companion-mv3" ext-id="liecbddmkiiihnedobmlmillhodjkdmb"><section id="shadow-host-companion"><template shadowrootmode="open"><div id="inner-shadow-companion"><div class="css-0" id="tooltip-mount-layer-companion"></div><style data-emotion="companion-global"></style><style data-emotion="companion" data-s=""></style><style>
            
    #inner-shadow-companion {
      font-size: 100%;
    }
    #inner-shadow-companion {
      font-family: circular, -apple-system, BlinkMacSystemFont, Segoe UI,
        sans-serif;
      color: var(--lns-color-body);
      
  font-size: var(--lns-fontSize-medium);
  line-height: var(--lns-lineHeight-medium);
;
      font-feature-settings: 'ss08' on;
    }

    #inner-shadow-companion *,
    #inner-shadow-companion *:before,
    #inner-shadow-companion *:after {
      box-sizing: border-box;
    }

    #inner-shadow-companion * {
      -webkit-font-smoothing: antialiased;
      -moz-osx-font-smoothing: grayscale;
      letter-spacing: calc(0.6px - 0.05em);
    }

    
    #inner-shadow-companion,
    .theme-light,
    [data-lens-theme="light"] {
      --lns-color-primary: var(--lns-themeLight-color-primary);--lns-color-primaryHover: var(--lns-themeLight-color-primaryHover);--lns-color-primaryActive: var(--lns-themeLight-color-primaryActive);--lns-color-body: var(--lns-themeLight-color-body);--lns-color-bodyDimmed: var(--lns-themeLight-color-bodyDimmed);--lns-color-background: var(--lns-themeLight-color-background);--lns-color-backgroundHover: var(--lns-themeLight-color-backgroundHover);--lns-color-backgroundActive: var(--lns-themeLight-color-backgroundActive);--lns-color-backgroundSecondary: var(--lns-themeLight-color-backgroundSecondary);--lns-color-backgroundSecondary2: var(--lns-themeLight-color-backgroundSecondary2);--lns-color-overlay: var(--lns-themeLight-color-overlay);--lns-color-border: var(--lns-themeLight-color-border);--lns-color-focusRing: var(--lns-themeLight-color-focusRing);--lns-color-record: var(--lns-themeLight-color-record);--lns-color-recordHover: var(--lns-themeLight-color-recordHover);--lns-color-recordActive: var(--lns-themeLight-color-recordActive);--lns-color-info: var(--lns-themeLight-color-info);--lns-color-success: var(--lns-themeLight-color-success);--lns-color-warning: var(--lns-themeLight-color-warning);--lns-color-danger: var(--lns-themeLight-color-danger);--lns-color-dangerHover: var(--lns-themeLight-color-dangerHover);--lns-color-dangerActive: var(--lns-themeLight-color-dangerActive);--lns-color-backdrop: var(--lns-themeLight-color-backdrop);--lns-color-backdropDark: var(--lns-themeLight-color-backdropDark);--lns-color-backdropTwilight: var(--lns-themeLight-color-backdropTwilight);--lns-color-disabledContent: var(--lns-themeLight-color-disabledContent);--lns-color-highlight: var(--lns-themeLight-color-highlight);--lns-color-disabledBackground: var(--lns-themeLight-color-disabledBackground);--lns-color-formFieldBorder: var(--lns-themeLight-color-formFieldBorder);--lns-color-formFieldBackground: var(--lns-themeLight-color-formFieldBackground);--lns-color-buttonBorder: var(--lns-themeLight-color-buttonBorder);--lns-color-upgrade: var(--lns-themeLight-color-upgrade);--lns-color-upgradeHover: var(--lns-themeLight-color-upgradeHover);--lns-color-upgradeActive: var(--lns-themeLight-color-upgradeActive);--lns-color-tabBackground: var(--lns-themeLight-color-tabBackground);--lns-color-discoveryBackground: var(--lns-themeLight-color-discoveryBackground);--lns-color-discoveryLightBackground: var(--lns-themeLight-color-discoveryLightBackground);--lns-color-discoveryTitle: var(--lns-themeLight-color-discoveryTitle);--lns-color-discoveryHighlight: var(--lns-themeLight-color-discoveryHighlight);
    }

    .theme-dark,
    [data-lens-theme="dark"] {
      --lns-color-primary: var(--lns-themeDark-color-primary);--lns-color-primaryHover: var(--lns-themeDark-color-primaryHover);--lns-color-primaryActive: var(--lns-themeDark-color-primaryActive);--lns-color-body: var(--lns-themeDark-color-body);--lns-color-bodyDimmed: var(--lns-themeDark-color-bodyDimmed);--lns-color-background: var(--lns-themeDark-color-background);--lns-color-backgroundHover: var(--lns-themeDark-color-backgroundHover);--lns-color-backgroundActive: var(--lns-themeDark-color-backgroundActive);--lns-color-backgroundSecondary: var(--lns-themeDark-color-backgroundSecondary);--lns-color-backgroundSecondary2: var(--lns-themeDark-color-backgroundSecondary2);--lns-color-overlay: var(--lns-themeDark-color-overlay);--lns-color-border: var(--lns-themeDark-color-border);--lns-color-focusRing: var(--lns-themeDark-color-focusRing);--lns-color-record: var(--lns-themeDark-color-record);--lns-color-recordHover: var(--lns-themeDark-color-recordHover);--lns-color-recordActive: var(--lns-themeDark-color-recordActive);--lns-color-info: var(--lns-themeDark-color-info);--lns-color-success: var(--lns-themeDark-color-success);--lns-color-warning: var(--lns-themeDark-color-warning);--lns-color-danger: var(--lns-themeDark-color-danger);--lns-color-dangerHover: var(--lns-themeDark-color-dangerHover);--lns-color-dangerActive: var(--lns-themeDark-color-dangerActive);--lns-color-backdrop: var(--lns-themeDark-color-backdrop);--lns-color-backdropDark: var(--lns-themeDark-color-backdropDark);--lns-color-backdropTwilight: var(--lns-themeDark-color-backdropTwilight);--lns-color-disabledContent: var(--lns-themeDark-color-disabledContent);--lns-color-highlight: var(--lns-themeDark-color-highlight);--lns-color-disabledBackground: var(--lns-themeDark-color-disabledBackground);--lns-color-formFieldBorder: var(--lns-themeDark-color-formFieldBorder);--lns-color-formFieldBackground: var(--lns-themeDark-color-formFieldBackground);--lns-color-buttonBorder: var(--lns-themeDark-color-buttonBorder);--lns-color-upgrade: var(--lns-themeDark-color-upgrade);--lns-color-upgradeHover: var(--lns-themeDark-color-upgradeHover);--lns-color-upgradeActive: var(--lns-themeDark-color-upgradeActive);--lns-color-tabBackground: var(--lns-themeDark-color-tabBackground);--lns-color-discoveryBackground: var(--lns-themeDark-color-discoveryBackground);--lns-color-discoveryLightBackground: var(--lns-themeDark-color-discoveryLightBackground);--lns-color-discoveryTitle: var(--lns-themeDark-color-discoveryTitle);--lns-color-discoveryHighlight: var(--lns-themeDark-color-discoveryHighlight);
    }
  

    
    #inner-shadow-companion {
      --lns-fontWeight-book:400;--lns-fontWeight-bold:700;--lns-unit:0.5rem;--lns-fontSize-small:calc(1.5 * var(--lns-unit, 8px));--lns-lineHeight-small:1.5;--lns-fontSize-body-sm:calc(1.5 * var(--lns-unit, 8px));--lns-lineHeight-body-sm:1.5;--lns-fontSize-medium:calc(1.75 * var(--lns-unit, 8px));--lns-lineHeight-medium:1.6;--lns-fontSize-body-md:calc(1.75 * var(--lns-unit, 8px));--lns-lineHeight-body-md:1.6;--lns-fontSize-large:calc(2.25 * var(--lns-unit, 8px));--lns-lineHeight-large:1.45;--lns-fontSize-body-lg:calc(2.25 * var(--lns-unit, 8px));--lns-lineHeight-body-lg:1.45;--lns-fontSize-xlarge:calc(3 * var(--lns-unit, 8px));--lns-lineHeight-xlarge:1.35;--lns-fontSize-heading-sm:calc(3 * var(--lns-unit, 8px));--lns-lineHeight-heading-sm:1.35;--lns-fontSize-xxlarge:calc(4 * var(--lns-unit, 8px));--lns-lineHeight-xxlarge:1.2;--lns-fontSize-heading-md:calc(4 * var(--lns-unit, 8px));--lns-lineHeight-heading-md:1.2;--lns-fontSize-xxxlarge:calc(6 * var(--lns-unit, 8px));--lns-lineHeight-xxxlarge:1.15;--lns-fontSize-heading-lg:calc(6 * var(--lns-unit, 8px));--lns-lineHeight-heading-lg:1.15;--lns-radius-medium:calc(1 * var(--lns-unit, 8px));--lns-radius-large:calc(2 * var(--lns-unit, 8px));--lns-radius-xlarge:calc(3 * var(--lns-unit, 8px));--lns-radius-full:calc(999 * var(--lns-unit, 8px));--lns-shadow-small:0 calc(0.5 * var(--lns-unit, 8px)) calc(1.25 * var(--lns-unit, 8px)) hsla(0, 0%, 0%, 0.05);--lns-shadow-medium:0 calc(0.5 * var(--lns-unit, 8px)) calc(1.25 * var(--lns-unit, 8px)) hsla(0, 0%, 0%, 0.1);--lns-shadow-large:0 calc(0.75 * var(--lns-unit, 8px)) calc(3 * var(--lns-unit, 8px)) hsla(0, 0%, 0%, 0.1);--lns-space-xsmall:calc(0.5 * var(--lns-unit, 8px));--lns-space-small:calc(1 * var(--lns-unit, 8px));--lns-space-medium:calc(2 * var(--lns-unit, 8px));--lns-space-large:calc(3 * var(--lns-unit, 8px));--lns-space-xlarge:calc(5 * var(--lns-unit, 8px));--lns-space-xxlarge:calc(8 * var(--lns-unit, 8px));--lns-formFieldBorderWidth:1px;--lns-formFieldBorderWidthFocus:2px;--lns-formFieldHeight:calc(4.5 * var(--lns-unit, 8px));--lns-formFieldRadius:calc(2.25 * var(--lns-unit, 8px));--lns-formFieldHorizontalPadding:calc(2 * var(--lns-unit, 8px));--lns-formFieldBorderShadow:
    inset 0 0 0 var(--lns-formFieldBorderWidth) var(--lns-color-formFieldBorder)
  ;--lns-formFieldBorderShadowFocus:
    inset 0 0 0 var(--lns-formFieldBorderWidthFocus) var(--lns-color-blurple),
    0 0 0 var(--lns-formFieldBorderWidthFocus) var(--lns-color-focusRing)
  ;--lns-color-red:hsla(11,80%,45%,1);--lns-color-blurpleLight:hsla(240,83.3%,95.3%,1);--lns-color-blurpleMedium:hsla(242,81%,87.6%,1);--lns-color-blurple:hsla(242,88.4%,66.3%,1);--lns-color-blurpleDark:hsla(242,87.6%,62%,1);--lns-color-offWhite:hsla(45,36.4%,95.7%,1);--lns-color-blueLight:hsla(206,58.3%,85.9%,1);--lns-color-blue:hsla(206,100%,73.3%,1);--lns-color-blueDark:hsla(206,29.5%,33.9%,1);--lns-color-orangeLight:hsla(6,100%,89.6%,1);--lns-color-orange:hsla(11,100%,62.2%,1);--lns-color-orangeDark:hsla(11,79.9%,64.9%,1);--lns-color-tealLight:hsla(180,20%,67.6%,1);--lns-color-teal:hsla(180,51.4%,51.6%,1);--lns-color-tealDark:hsla(180,16.2%,22.9%,1);--lns-color-yellowLight:hsla(39,100%,87.8%,1);--lns-color-yellow:hsla(50,100%,57.3%,1);--lns-color-yellowDark:hsla(39,100%,68%,1);--lns-color-grey8:hsla(0,0%,13%,1);--lns-color-grey7:hsla(246,16%,26%,1);--lns-color-grey6:hsla(252,13%,46%,1);--lns-color-grey5:hsla(240,7%,62%,1);--lns-color-grey4:hsla(259,12%,75%,1);--lns-color-grey3:hsla(260,11%,85%,1);--lns-color-grey2:hsla(260,11%,95%,1);--lns-color-grey1:hsla(240,7%,97%,1);--lns-color-white:hsla(0,0%,100%,1);--lns-themeLight-color-primary:hsla(242,88.4%,66.3%,1);--lns-themeLight-color-primaryHover:hsla(242,88.4%,56.3%,1);--lns-themeLight-color-primaryActive:hsla(242,88.4%,45.3%,1);--lns-themeLight-color-body:hsla(0,0%,13%,1);--lns-themeLight-color-bodyDimmed:hsla(252,13%,46%,1);--lns-themeLight-color-background:hsla(0,0%,100%,1);--lns-themeLight-color-backgroundHover:hsla(246,16%,26%,0.1);--lns-themeLight-color-backgroundActive:hsla(246,16%,26%,0.3);--lns-themeLight-color-backgroundSecondary:hsla(246,16%,26%,0.04);--lns-themeLight-color-backgroundSecondary2:hsla(45,34%,78%,0.2);--lns-themeLight-color-overlay:hsla(0,0%,100%,1);--lns-themeLight-color-border:hsla(252,13%,46%,0.2);--lns-themeLight-color-focusRing:hsla(242,88.4%,66.3%,0.5);--lns-themeLight-color-record:hsla(11,100%,62.2%,1);--lns-themeLight-color-recordHover:hsla(11,100%,52.2%,1);--lns-themeLight-color-recordActive:hsla(11,100%,42.2%,1);--lns-themeLight-color-info:hsla(206,100%,73.3%,1);--lns-themeLight-color-success:hsla(180,51.4%,51.6%,1);--lns-themeLight-color-warning:hsla(39,100%,68%,1);--lns-themeLight-color-danger:hsla(11,80%,45%,1);--lns-themeLight-color-dangerHover:hsla(11,80%,38%,1);--lns-themeLight-color-dangerActive:hsla(11,80%,31%,1);--lns-themeLight-color-backdrop:hsla(0,0%,13%,0.5);--lns-themeLight-color-backdropDark:hsla(0,0%,13%,0.9);--lns-themeLight-color-backdropTwilight:hsla(245,44.8%,46.9%,0.8);--lns-themeLight-color-disabledContent:hsla(240,7%,62%,1);--lns-themeLight-color-highlight:hsla(240,83.3%,66.3%,0.15);--lns-themeLight-color-disabledBackground:hsla(260,11%,95%,1);--lns-themeLight-color-formFieldBorder:hsla(260,11%,85%,1);--lns-themeLight-color-formFieldBackground:hsla(0,0%,100%,1);--lns-themeLight-color-buttonBorder:hsla(252,13%,46%,0.25);--lns-themeLight-color-upgrade:hsla(206,100%,93%,1);--lns-themeLight-color-upgradeHover:hsla(206,100%,85%,1);--lns-themeLight-color-upgradeActive:hsla(206,100%,77%,1);--lns-themeLight-color-tabBackground:hsla(252,13%,46%,0.15);--lns-themeLight-color-discoveryBackground:hsla(206,100%,93%,1);--lns-themeLight-color-discoveryLightBackground:hsla(206,100%,97%,1);--lns-themeLight-color-discoveryTitle:hsla(0,0%,13%,1);--lns-themeLight-color-discoveryHighlight:hsla(206,100%,77%,0.3);--lns-themeDark-color-primary:hsla(242,87%,73%,1);--lns-themeDark-color-primaryHover:hsla(242,88.4%,56.3%,1);--lns-themeDark-color-primaryActive:hsla(242,88.4%,45.3%,1);--lns-themeDark-color-body:hsla(240,7%,97%,1);--lns-themeDark-color-bodyDimmed:hsla(240,7%,62%,1);--lns-themeDark-color-background:hsla(0,0%,13%,1);--lns-themeDark-color-backgroundHover:hsla(0,0%,100%,0.1);--lns-themeDark-color-backgroundActive:hsla(0,0%,100%,0.2);--lns-themeDark-color-backgroundSecondary:hsla(0,0%,100%,0.04);--lns-themeDark-color-backgroundSecondary2:hsla(45,13%,44%,0.2);--lns-themeDark-color-overlay:hsla(0,0%,20%,1);--lns-themeDark-color-border:hsla(259,12%,75%,0.2);--lns-themeDark-color-focusRing:hsla(242,88.4%,66.3%,0.5);--lns-themeDark-color-record:hsla(11,100%,62.2%,1);--lns-themeDark-color-recordHover:hsla(11,100%,52.2%,1);--lns-themeDark-color-recordActive:hsla(11,100%,42.2%,1);--lns-themeDark-color-info:hsla(206,100%,73.3%,1);--lns-themeDark-color-success:hsla(180,51.4%,51.6%,1);--lns-themeDark-color-warning:hsla(39,100%,68%,1);--lns-themeDark-color-danger:hsla(11,80%,45%,1);--lns-themeDark-color-dangerHover:hsla(11,80%,38%,1);--lns-themeDark-color-dangerActive:hsla(11,80%,31%,1);--lns-themeDark-color-backdrop:hsla(0,0%,13%,0.5);--lns-themeDark-color-backdropDark:hsla(0,0%,13%,0.9);--lns-themeDark-color-backdropTwilight:hsla(245,44.8%,46.9%,0.8);--lns-themeDark-color-disabledContent:hsla(240,7%,62%,1);--lns-themeDark-color-highlight:hsla(240,83.3%,66.3%,0.15);--lns-themeDark-color-disabledBackground:hsla(252,13%,23%,1);--lns-themeDark-color-formFieldBorder:hsla(252,13%,46%,1);--lns-themeDark-color-formFieldBackground:hsla(0,0%,13%,1);--lns-themeDark-color-buttonBorder:hsla(0,0%,100%,0.25);--lns-themeDark-color-upgrade:hsla(206,92%,81%,1);--lns-themeDark-color-upgradeHover:hsla(206,92%,74%,1);--lns-themeDark-color-upgradeActive:hsla(206,92%,67%,1);--lns-themeDark-color-tabBackground:hsla(0,0%,100%,0.15);--lns-themeDark-color-discoveryBackground:hsla(206,92%,81%,1);--lns-themeDark-color-discoveryLightBackground:hsla(0,0%,13%,1);--lns-themeDark-color-discoveryTitle:hsla(206,100%,73.3%,1);--lns-themeDark-color-discoveryHighlight:hsla(206,100%,77%,0.3);
    }
  

    .c\:red{color:var(--lns-color-red)}.c\:blurpleLight{color:var(--lns-color-blurpleLight)}.c\:blurpleMedium{color:var(--lns-color-blurpleMedium)}.c\:blurple{color:var(--lns-color-blurple)}.c\:blurpleDark{color:var(--lns-color-blurpleDark)}.c\:offWhite{color:var(--lns-color-offWhite)}.c\:blueLight{color:var(--lns-color-blueLight)}.c\:blue{color:var(--lns-color-blue)}.c\:blueDark{color:var(--lns-color-blueDark)}.c\:orangeLight{color:var(--lns-color-orangeLight)}.c\:orange{color:var(--lns-color-orange)}.c\:orangeDark{color:var(--lns-color-orangeDark)}.c\:tealLight{color:var(--lns-color-tealLight)}.c\:teal{color:var(--lns-color-teal)}.c\:tealDark{color:var(--lns-color-tealDark)}.c\:yellowLight{color:var(--lns-color-yellowLight)}.c\:yellow{color:var(--lns-color-yellow)}.c\:yellowDark{color:var(--lns-color-yellowDark)}.c\:grey8{color:var(--lns-color-grey8)}.c\:grey7{color:var(--lns-color-grey7)}.c\:grey6{color:var(--lns-color-grey6)}.c\:grey5{color:var(--lns-color-grey5)}.c\:grey4{color:var(--lns-color-grey4)}.c\:grey3{color:var(--lns-color-grey3)}.c\:grey2{color:var(--lns-color-grey2)}.c\:grey1{color:var(--lns-color-grey1)}.c\:white{color:var(--lns-color-white)}.c\:primary{color:var(--lns-color-primary)}.c\:primaryHover{color:var(--lns-color-primaryHover)}.c\:primaryActive{color:var(--lns-color-primaryActive)}.c\:body{color:var(--lns-color-body)}.c\:bodyDimmed{color:var(--lns-color-bodyDimmed)}.c\:background{color:var(--lns-color-background)}.c\:backgroundHover{color:var(--lns-color-backgroundHover)}.c\:backgroundActive{color:var(--lns-color-backgroundActive)}.c\:backgroundSecondary{color:var(--lns-color-backgroundSecondary)}.c\:backgroundSecondary2{color:var(--lns-color-backgroundSecondary2)}.c\:overlay{color:var(--lns-color-overlay)}.c\:border{color:var(--lns-color-border)}.c\:focusRing{color:var(--lns-color-focusRing)}.c\:record{color:var(--lns-color-record)}.c\:recordHover{color:var(--lns-color-recordHover)}.c\:recordActive{color:var(--lns-color-recordActive)}.c\:info{color:var(--lns-color-info)}.c\:success{color:var(--lns-color-success)}.c\:warning{color:var(--lns-color-warning)}.c\:danger{color:var(--lns-color-danger)}.c\:dangerHover{color:var(--lns-color-dangerHover)}.c\:dangerActive{color:var(--lns-color-dangerActive)}.c\:backdrop{color:var(--lns-color-backdrop)}.c\:backdropDark{color:var(--lns-color-backdropDark)}.c\:backdropTwilight{color:var(--lns-color-backdropTwilight)}.c\:disabledContent{color:var(--lns-color-disabledContent)}.c\:highlight{color:var(--lns-color-highlight)}.c\:disabledBackground{color:var(--lns-color-disabledBackground)}.c\:formFieldBorder{color:var(--lns-color-formFieldBorder)}.c\:formFieldBackground{color:var(--lns-color-formFieldBackground)}.c\:buttonBorder{color:var(--lns-color-buttonBorder)}.c\:upgrade{color:var(--lns-color-upgrade)}.c\:upgradeHover{color:var(--lns-color-upgradeHover)}.c\:upgradeActive{color:var(--lns-color-upgradeActive)}.c\:tabBackground{color:var(--lns-color-tabBackground)}.c\:discoveryBackground{color:var(--lns-color-discoveryBackground)}.c\:discoveryLightBackground{color:var(--lns-color-discoveryLightBackground)}.c\:discoveryTitle{color:var(--lns-color-discoveryTitle)}.c\:discoveryHighlight{color:var(--lns-color-discoveryHighlight)}.shadow\:small{box-shadow:var(--lns-shadow-small)}.shadow\:medium{box-shadow:var(--lns-shadow-medium)}.shadow\:large{box-shadow:var(--lns-shadow-large)}.radius\:medium{border-radius:var(--lns-radius-medium)}.radius\:large{border-radius:var(--lns-radius-large)}.radius\:xlarge{border-radius:var(--lns-radius-xlarge)}.radius\:full{border-radius:var(--lns-radius-full)}.bgc\:red{background-color:var(--lns-color-red)}.bgc\:blurpleLight{background-color:var(--lns-color-blurpleLight)}.bgc\:blurpleMedium{background-color:var(--lns-color-blurpleMedium)}.bgc\:blurple{background-color:var(--lns-color-blurple)}.bgc\:blurpleDark{background-color:var(--lns-color-blurpleDark)}.bgc\:offWhite{background-color:var(--lns-color-offWhite)}.bgc\:blueLight{background-color:var(--lns-color-blueLight)}.bgc\:blue{background-color:var(--lns-color-blue)}.bgc\:blueDark{background-color:var(--lns-color-blueDark)}.bgc\:orangeLight{background-color:var(--lns-color-orangeLight)}.bgc\:orange{background-color:var(--lns-color-orange)}.bgc\:orangeDark{background-color:var(--lns-color-orangeDark)}.bgc\:tealLight{background-color:var(--lns-color-tealLight)}.bgc\:teal{background-color:var(--lns-color-teal)}.bgc\:tealDark{background-color:var(--lns-color-tealDark)}.bgc\:yellowLight{background-color:var(--lns-color-yellowLight)}.bgc\:yellow{background-color:var(--lns-color-yellow)}.bgc\:yellowDark{background-color:var(--lns-color-yellowDark)}.bgc\:grey8{background-color:var(--lns-color-grey8)}.bgc\:grey7{background-color:var(--lns-color-grey7)}.bgc\:grey6{background-color:var(--lns-color-grey6)}.bgc\:grey5{background-color:var(--lns-color-grey5)}.bgc\:grey4{background-color:var(--lns-color-grey4)}.bgc\:grey3{background-color:var(--lns-color-grey3)}.bgc\:grey2{background-color:var(--lns-color-grey2)}.bgc\:grey1{background-color:var(--lns-color-grey1)}.bgc\:white{background-color:var(--lns-color-white)}.bgc\:primary{background-color:var(--lns-color-primary)}.bgc\:primaryHover{background-color:var(--lns-color-primaryHover)}.bgc\:primaryActive{background-color:var(--lns-color-primaryActive)}.bgc\:body{background-color:var(--lns-color-body)}.bgc\:bodyDimmed{background-color:var(--lns-color-bodyDimmed)}.bgc\:background{background-color:var(--lns-color-background)}.bgc\:backgroundHover{background-color:var(--lns-color-backgroundHover)}.bgc\:backgroundActive{background-color:var(--lns-color-backgroundActive)}.bgc\:backgroundSecondary{background-color:var(--lns-color-backgroundSecondary)}.bgc\:backgroundSecondary2{background-color:var(--lns-color-backgroundSecondary2)}.bgc\:overlay{background-color:var(--lns-color-overlay)}.bgc\:border{background-color:var(--lns-color-border)}.bgc\:focusRing{background-color:var(--lns-color-focusRing)}.bgc\:record{background-color:var(--lns-color-record)}.bgc\:recordHover{background-color:var(--lns-color-recordHover)}.bgc\:recordActive{background-color:var(--lns-color-recordActive)}.bgc\:info{background-color:var(--lns-color-info)}.bgc\:success{background-color:var(--lns-color-success)}.bgc\:warning{background-color:var(--lns-color-warning)}.bgc\:danger{background-color:var(--lns-color-danger)}.bgc\:dangerHover{background-color:var(--lns-color-dangerHover)}.bgc\:dangerActive{background-color:var(--lns-color-dangerActive)}.bgc\:backdrop{background-color:var(--lns-color-backdrop)}.bgc\:backdropDark{background-color:var(--lns-color-backdropDark)}.bgc\:backdropTwilight{background-color:var(--lns-color-backdropTwilight)}.bgc\:disabledContent{background-color:var(--lns-color-disabledContent)}.bgc\:highlight{background-color:var(--lns-color-highlight)}.bgc\:disabledBackground{background-color:var(--lns-color-disabledBackground)}.bgc\:formFieldBorder{background-color:var(--lns-color-formFieldBorder)}.bgc\:formFieldBackground{background-color:var(--lns-color-formFieldBackground)}.bgc\:buttonBorder{background-color:var(--lns-color-buttonBorder)}.bgc\:upgrade{background-color:var(--lns-color-upgrade)}.bgc\:upgradeHover{background-color:var(--lns-color-upgradeHover)}.bgc\:upgradeActive{background-color:var(--lns-color-upgradeActive)}.bgc\:tabBackground{background-color:var(--lns-color-tabBackground)}.bgc\:discoveryBackground{background-color:var(--lns-color-discoveryBackground)}.bgc\:discoveryLightBackground{background-color:var(--lns-color-discoveryLightBackground)}.bgc\:discoveryTitle{background-color:var(--lns-color-discoveryTitle)}.bgc\:discoveryHighlight{background-color:var(--lns-color-discoveryHighlight)}.m\:0{margin:0}.m\:auto{margin:auto}.m\:xsmall{margin:var(--lns-space-xsmall)}.m\:small{margin:var(--lns-space-small)}.m\:medium{margin:var(--lns-space-medium)}.m\:large{margin:var(--lns-space-large)}.m\:xlarge{margin:var(--lns-space-xlarge)}.m\:xxlarge{margin:var(--lns-space-xxlarge)}.mt\:0{margin-top:0}.mt\:auto{margin-top:auto}.mt\:xsmall{margin-top:var(--lns-space-xsmall)}.mt\:small{margin-top:var(--lns-space-small)}.mt\:medium{margin-top:var(--lns-space-medium)}.mt\:large{margin-top:var(--lns-space-large)}.mt\:xlarge{margin-top:var(--lns-space-xlarge)}.mt\:xxlarge{margin-top:var(--lns-space-xxlarge)}.mb\:0{margin-bottom:0}.mb\:auto{margin-bottom:auto}.mb\:xsmall{margin-bottom:var(--lns-space-xsmall)}.mb\:small{margin-bottom:var(--lns-space-small)}.mb\:medium{margin-bottom:var(--lns-space-medium)}.mb\:large{margin-bottom:var(--lns-space-large)}.mb\:xlarge{margin-bottom:var(--lns-space-xlarge)}.mb\:xxlarge{margin-bottom:var(--lns-space-xxlarge)}.ml\:0{margin-left:0}.ml\:auto{margin-left:auto}.ml\:xsmall{margin-left:var(--lns-space-xsmall)}.ml\:small{margin-left:var(--lns-space-small)}.ml\:medium{margin-left:var(--lns-space-medium)}.ml\:large{margin-left:var(--lns-space-large)}.ml\:xlarge{margin-left:var(--lns-space-xlarge)}.ml\:xxlarge{margin-left:var(--lns-space-xxlarge)}.mr\:0{margin-right:0}.mr\:auto{margin-right:auto}.mr\:xsmall{margin-right:var(--lns-space-xsmall)}.mr\:small{margin-right:var(--lns-space-small)}.mr\:medium{margin-right:var(--lns-space-medium)}.mr\:large{margin-right:var(--lns-space-large)}.mr\:xlarge{margin-right:var(--lns-space-xlarge)}.mr\:xxlarge{margin-right:var(--lns-space-xxlarge)}.mx\:0{margin-left:0;margin-right:0}.mx\:auto{margin-left:auto;margin-right:auto}.mx\:xsmall{margin-left:var(--lns-space-xsmall);margin-right:var(--lns-space-xsmall)}.mx\:small{margin-left:var(--lns-space-small);margin-right:var(--lns-space-small)}.mx\:medium{margin-left:var(--lns-space-medium);margin-right:var(--lns-space-medium)}.mx\:large{margin-left:var(--lns-space-large);margin-right:var(--lns-space-large)}.mx\:xlarge{margin-left:var(--lns-space-xlarge);margin-right:var(--lns-space-xlarge)}.mx\:xxlarge{margin-left:var(--lns-space-xxlarge);margin-right:var(--lns-space-xxlarge)}.my\:0{margin-top:0;margin-bottom:0}.my\:auto{margin-top:auto;margin-bottom:auto}.my\:xsmall{margin-top:var(--lns-space-xsmall);margin-bottom:var(--lns-space-xsmall)}.my\:small{margin-top:var(--lns-space-small);margin-bottom:var(--lns-space-small)}.my\:medium{margin-top:var(--lns-space-medium);margin-bottom:var(--lns-space-medium)}.my\:large{margin-top:var(--lns-space-large);margin-bottom:var(--lns-space-large)}.my\:xlarge{margin-top:var(--lns-space-xlarge);margin-bottom:var(--lns-space-xlarge)}.my\:xxlarge{margin-top:var(--lns-space-xxlarge);margin-bottom:var(--lns-space-xxlarge)}.p\:0{padding:0}.p\:xsmall{padding:var(--lns-space-xsmall)}.p\:small{padding:var(--lns-space-small)}.p\:medium{padding:var(--lns-space-medium)}.p\:large{padding:var(--lns-space-large)}.p\:xlarge{padding:var(--lns-space-xlarge)}.p\:xxlarge{padding:var(--lns-space-xxlarge)}.pt\:0{padding-top:0}.pt\:xsmall{padding-top:var(--lns-space-xsmall)}.pt\:small{padding-top:var(--lns-space-small)}.pt\:medium{padding-top:var(--lns-space-medium)}.pt\:large{padding-top:var(--lns-space-large)}.pt\:xlarge{padding-top:var(--lns-space-xlarge)}.pt\:xxlarge{padding-top:var(--lns-space-xxlarge)}.pb\:0{padding-bottom:0}.pb\:xsmall{padding-bottom:var(--lns-space-xsmall)}.pb\:small{padding-bottom:var(--lns-space-small)}.pb\:medium{padding-bottom:var(--lns-space-medium)}.pb\:large{padding-bottom:var(--lns-space-large)}.pb\:xlarge{padding-bottom:var(--lns-space-xlarge)}.pb\:xxlarge{padding-bottom:var(--lns-space-xxlarge)}.pl\:0{padding-left:0}.pl\:xsmall{padding-left:var(--lns-space-xsmall)}.pl\:small{padding-left:var(--lns-space-small)}.pl\:medium{padding-left:var(--lns-space-medium)}.pl\:large{padding-left:var(--lns-space-large)}.pl\:xlarge{padding-left:var(--lns-space-xlarge)}.pl\:xxlarge{padding-left:var(--lns-space-xxlarge)}.pr\:0{padding-right:0}.pr\:xsmall{padding-right:var(--lns-space-xsmall)}.pr\:small{padding-right:var(--lns-space-small)}.pr\:medium{padding-right:var(--lns-space-medium)}.pr\:large{padding-right:var(--lns-space-large)}.pr\:xlarge{padding-right:var(--lns-space-xlarge)}.pr\:xxlarge{padding-right:var(--lns-space-xxlarge)}.px\:0{padding-left:0;padding-right:0}.px\:xsmall{padding-left:var(--lns-space-xsmall);padding-right:var(--lns-space-xsmall)}.px\:small{padding-left:var(--lns-space-small);padding-right:var(--lns-space-small)}.px\:medium{padding-left:var(--lns-space-medium);padding-right:var(--lns-space-medium)}.px\:large{padding-left:var(--lns-space-large);padding-right:var(--lns-space-large)}.px\:xlarge{padding-left:var(--lns-space-xlarge);padding-right:var(--lns-space-xlarge)}.px\:xxlarge{padding-left:var(--lns-space-xxlarge);padding-right:var(--lns-space-xxlarge)}.py\:0{padding-top:0;padding-bottom:0}.py\:xsmall{padding-top:var(--lns-space-xsmall);padding-bottom:var(--lns-space-xsmall)}.py\:small{padding-top:var(--lns-space-small);padding-bottom:var(--lns-space-small)}.py\:medium{padding-top:var(--lns-space-medium);padding-bottom:var(--lns-space-medium)}.py\:large{padding-top:var(--lns-space-large);padding-bottom:var(--lns-space-large)}.py\:xlarge{padding-top:var(--lns-space-xlarge);padding-bottom:var(--lns-space-xlarge)}.py\:xxlarge{padding-top:var(--lns-space-xxlarge);padding-bottom:var(--lns-space-xxlarge)}.text\:small{font-size:var(--lns-fontSize-small);line-height:var(--lns-lineHeight-small)}.text\:body-sm{font-size:var(--lns-fontSize-body-sm);line-height:var(--lns-lineHeight-body-sm)}.text\:medium{font-size:var(--lns-fontSize-medium);line-height:var(--lns-lineHeight-medium)}.text\:body-md{font-size:var(--lns-fontSize-body-md);line-height:var(--lns-lineHeight-body-md)}.text\:large{font-size:var(--lns-fontSize-large);line-height:var(--lns-lineHeight-large)}.text\:body-lg{font-size:var(--lns-fontSize-body-lg);line-height:var(--lns-lineHeight-body-lg)}.text\:xlarge{font-size:var(--lns-fontSize-xlarge);line-height:var(--lns-lineHeight-xlarge)}.text\:heading-sm{font-size:var(--lns-fontSize-heading-sm);line-height:var(--lns-lineHeight-heading-sm)}.text\:xxlarge{font-size:var(--lns-fontSize-xxlarge);line-height:var(--lns-lineHeight-xxlarge)}.text\:heading-md{font-size:var(--lns-fontSize-heading-md);line-height:var(--lns-lineHeight-heading-md)}.text\:xxxlarge{font-size:var(--lns-fontSize-xxxlarge);line-height:var(--lns-lineHeight-xxxlarge)}.text\:heading-lg{font-size:var(--lns-fontSize-heading-lg);line-height:var(--lns-lineHeight-heading-lg)}.weight\:book{font-weight:var(--lns-fontWeight-book)}.weight\:bold{font-weight:var(--lns-fontWeight-bold)}.text\:body{font-size:var(--lns-fontSize-body-md);line-height:var(--lns-lineHeight-body-md);font-weight:var(--lns-fontWeight-book)}.text\:title{font-size:var(--lns-fontSize-body-lg);line-height:var(--lns-lineHeight-body-lg);font-weight:var(--lns-fontWeight-bold)}.text\:mainTitle{font-size:var(--lns-fontSize-heading-md);line-height:var(--lns-lineHeight-heading-md);font-weight:var(--lns-fontWeight-bold)}.text\:left{text-align:left}.text\:right{text-align:right}.text\:center{text-align:center}.border{border:1px solid var(--lns-color-border)}.borderTop{border-top:1px solid var(--lns-color-border)}.borderBottom{border-bottom:1px solid var(--lns-color-border)}.borderLeft{border-left:1px solid var(--lns-color-border)}.borderRight{border-right:1px solid var(--lns-color-border)}.inline{display:inline}.block{display:block}.flex{display:flex}.inlineBlock{display:inline-block}.inlineFlex{display:inline-flex}.none{display:none}.flexWrap{flex-wrap:wrap}.flexDirection\:column{flex-direction:column}.flexDirection\:row{flex-direction:row}.items\:stretch{align-items:stretch}.items\:center{align-items:center}.items\:baseline{align-items:baseline}.items\:flexStart{align-items:flex-start}.items\:flexEnd{align-items:flex-end}.items\:selfStart{align-items:self-start}.items\:selfEnd{align-items:self-end}.justify\:flexStart{justify-content:flex-start}.justify\:flexEnd{justify-content:flex-end}.justify\:center{justify-content:center}.justify\:spaceBetween{justify-content:space-between}.justify\:spaceAround{justify-content:space-around}.justify\:spaceEvenly{justify-content:space-evenly}.grow\:0{flex-grow:0}.grow\:1{flex-grow:1}.shrink\:0{flex-shrink:0}.shrink\:1{flex-shrink:1}.self\:auto{align-self:auto}.self\:flexStart{align-self:flex-start}.self\:flexEnd{align-self:flex-end}.self\:center{align-self:center}.self\:baseline{align-self:baseline}.self\:stretch{align-self:stretch}.overflow\:hidden{overflow:hidden}.overflow\:auto{overflow:auto}.relative{position:relative}.absolute{position:absolute}.sticky{position:sticky}.fixed{position:fixed}.top\:0{top:0}.top\:auto{top:auto}.top\:xsmall{top:var(--lns-space-xsmall)}.top\:small{top:var(--lns-space-small)}.top\:medium{top:var(--lns-space-medium)}.top\:large{top:var(--lns-space-large)}.top\:xlarge{top:var(--lns-space-xlarge)}.top\:xxlarge{top:var(--lns-space-xxlarge)}.bottom\:0{bottom:0}.bottom\:auto{bottom:auto}.bottom\:xsmall{bottom:var(--lns-space-xsmall)}.bottom\:small{bottom:var(--lns-space-small)}.bottom\:medium{bottom:var(--lns-space-medium)}.bottom\:large{bottom:var(--lns-space-large)}.bottom\:xlarge{bottom:var(--lns-space-xlarge)}.bottom\:xxlarge{bottom:var(--lns-space-xxlarge)}.left\:0{left:0}.left\:auto{left:auto}.left\:xsmall{left:var(--lns-space-xsmall)}.left\:small{left:var(--lns-space-small)}.left\:medium{left:var(--lns-space-medium)}.left\:large{left:var(--lns-space-large)}.left\:xlarge{left:var(--lns-space-xlarge)}.left\:xxlarge{left:var(--lns-space-xxlarge)}.right\:0{right:0}.right\:auto{right:auto}.right\:xsmall{right:var(--lns-space-xsmall)}.right\:small{right:var(--lns-space-small)}.right\:medium{right:var(--lns-space-medium)}.right\:large{right:var(--lns-space-large)}.right\:xlarge{right:var(--lns-space-xlarge)}.right\:xxlarge{right:var(--lns-space-xxlarge)}.width\:auto{width:auto}.width\:full{width:100%}.width\:0{width:0}.minWidth\:0{min-width:0}.height\:auto{height:auto}.height\:full{height:100%}.height\:0{height:0}.ellipsis{overflow:hidden;text-overflow:ellipsis;white-space:nowrap}.srOnly{position:absolute;width:1px;height:1px;padding:0;margin:-1px;overflow:hidden;clip:rect(0, 0, 0, 0);white-space:nowrap;border-width:0}@media(min-width:31em){.xs-c\:red{color:var(--lns-color-red)}.xs-c\:blurpleLight{color:var(--lns-color-blurpleLight)}.xs-c\:blurpleMedium{color:var(--lns-color-blurpleMedium)}.xs-c\:blurple{color:var(--lns-color-blurple)}.xs-c\:blurpleDark{color:var(--lns-color-blurpleDark)}.xs-c\:offWhite{color:var(--lns-color-offWhite)}.xs-c\:blueLight{color:var(--lns-color-blueLight)}.xs-c\:blue{color:var(--lns-color-blue)}.xs-c\:blueDark{color:var(--lns-color-blueDark)}.xs-c\:orangeLight{color:var(--lns-color-orangeLight)}.xs-c\:orange{color:var(--lns-color-orange)}.xs-c\:orangeDark{color:var(--lns-color-orangeDark)}.xs-c\:tealLight{color:var(--lns-color-tealLight)}.xs-c\:teal{color:var(--lns-color-teal)}.xs-c\:tealDark{color:var(--lns-color-tealDark)}.xs-c\:yellowLight{color:var(--lns-color-yellowLight)}.xs-c\:yellow{color:var(--lns-color-yellow)}.xs-c\:yellowDark{color:var(--lns-color-yellowDark)}.xs-c\:grey8{color:var(--lns-color-grey8)}.xs-c\:grey7{color:var(--lns-color-grey7)}.xs-c\:grey6{color:var(--lns-color-grey6)}.xs-c\:grey5{color:var(--lns-color-grey5)}.xs-c\:grey4{color:var(--lns-color-grey4)}.xs-c\:grey3{color:var(--lns-color-grey3)}.xs-c\:grey2{color:var(--lns-color-grey2)}.xs-c\:grey1{color:var(--lns-color-grey1)}.xs-c\:white{color:var(--lns-color-white)}.xs-c\:primary{color:var(--lns-color-primary)}.xs-c\:primaryHover{color:var(--lns-color-primaryHover)}.xs-c\:primaryActive{color:var(--lns-color-primaryActive)}.xs-c\:body{color:var(--lns-color-body)}.xs-c\:bodyDimmed{color:var(--lns-color-bodyDimmed)}.xs-c\:background{color:var(--lns-color-background)}.xs-c\:backgroundHover{color:var(--lns-color-backgroundHover)}.xs-c\:backgroundActive{color:var(--lns-color-backgroundActive)}.xs-c\:backgroundSecondary{color:var(--lns-color-backgroundSecondary)}.xs-c\:backgroundSecondary2{color:var(--lns-color-backgroundSecondary2)}.xs-c\:overlay{color:var(--lns-color-overlay)}.xs-c\:border{color:var(--lns-color-border)}.xs-c\:focusRing{color:var(--lns-color-focusRing)}.xs-c\:record{color:var(--lns-color-record)}.xs-c\:recordHover{color:var(--lns-color-recordHover)}.xs-c\:recordActive{color:var(--lns-color-recordActive)}.xs-c\:info{color:var(--lns-color-info)}.xs-c\:success{color:var(--lns-color-success)}.xs-c\:warning{color:var(--lns-color-warning)}.xs-c\:danger{color:var(--lns-color-danger)}.xs-c\:dangerHover{color:var(--lns-color-dangerHover)}.xs-c\:dangerActive{color:var(--lns-color-dangerActive)}.xs-c\:backdrop{color:var(--lns-color-backdrop)}.xs-c\:backdropDark{color:var(--lns-color-backdropDark)}.xs-c\:backdropTwilight{color:var(--lns-color-backdropTwilight)}.xs-c\:disabledContent{color:var(--lns-color-disabledContent)}.xs-c\:highlight{color:var(--lns-color-highlight)}.xs-c\:disabledBackground{color:var(--lns-color-disabledBackground)}.xs-c\:formFieldBorder{color:var(--lns-color-formFieldBorder)}.xs-c\:formFieldBackground{color:var(--lns-color-formFieldBackground)}.xs-c\:buttonBorder{color:var(--lns-color-buttonBorder)}.xs-c\:upgrade{color:var(--lns-color-upgrade)}.xs-c\:upgradeHover{color:var(--lns-color-upgradeHover)}.xs-c\:upgradeActive{color:var(--lns-color-upgradeActive)}.xs-c\:tabBackground{color:var(--lns-color-tabBackground)}.xs-c\:discoveryBackground{color:var(--lns-color-discoveryBackground)}.xs-c\:discoveryLightBackground{color:var(--lns-color-discoveryLightBackground)}.xs-c\:discoveryTitle{color:var(--lns-color-discoveryTitle)}.xs-c\:discoveryHighlight{color:var(--lns-color-discoveryHighlight)}.xs-shadow\:small{box-shadow:var(--lns-shadow-small)}.xs-shadow\:medium{box-shadow:var(--lns-shadow-medium)}.xs-shadow\:large{box-shadow:var(--lns-shadow-large)}.xs-radius\:medium{border-radius:var(--lns-radius-medium)}.xs-radius\:large{border-radius:var(--lns-radius-large)}.xs-radius\:xlarge{border-radius:var(--lns-radius-xlarge)}.xs-radius\:full{border-radius:var(--lns-radius-full)}.xs-bgc\:red{background-color:var(--lns-color-red)}.xs-bgc\:blurpleLight{background-color:var(--lns-color-blurpleLight)}.xs-bgc\:blurpleMedium{background-color:var(--lns-color-blurpleMedium)}.xs-bgc\:blurple{background-color:var(--lns-color-blurple)}.xs-bgc\:blurpleDark{background-color:var(--lns-color-blurpleDark)}.xs-bgc\:offWhite{background-color:var(--lns-color-offWhite)}.xs-bgc\:blueLight{background-color:var(--lns-color-blueLight)}.xs-bgc\:blue{background-color:var(--lns-color-blue)}.xs-bgc\:blueDark{background-color:var(--lns-color-blueDark)}.xs-bgc\:orangeLight{background-color:var(--lns-color-orangeLight)}.xs-bgc\:orange{background-color:var(--lns-color-orange)}.xs-bgc\:orangeDark{background-color:var(--lns-color-orangeDark)}.xs-bgc\:tealLight{background-color:var(--lns-color-tealLight)}.xs-bgc\:teal{background-color:var(--lns-color-teal)}.xs-bgc\:tealDark{background-color:var(--lns-color-tealDark)}.xs-bgc\:yellowLight{background-color:var(--lns-color-yellowLight)}.xs-bgc\:yellow{background-color:var(--lns-color-yellow)}.xs-bgc\:yellowDark{background-color:var(--lns-color-yellowDark)}.xs-bgc\:grey8{background-color:var(--lns-color-grey8)}.xs-bgc\:grey7{background-color:var(--lns-color-grey7)}.xs-bgc\:grey6{background-color:var(--lns-color-grey6)}.xs-bgc\:grey5{background-color:var(--lns-color-grey5)}.xs-bgc\:grey4{background-color:var(--lns-color-grey4)}.xs-bgc\:grey3{background-color:var(--lns-color-grey3)}.xs-bgc\:grey2{background-color:var(--lns-color-grey2)}.xs-bgc\:grey1{background-color:var(--lns-color-grey1)}.xs-bgc\:white{background-color:var(--lns-color-white)}.xs-bgc\:primary{background-color:var(--lns-color-primary)}.xs-bgc\:primaryHover{background-color:var(--lns-color-primaryHover)}.xs-bgc\:primaryActive{background-color:var(--lns-color-primaryActive)}.xs-bgc\:body{background-color:var(--lns-color-body)}.xs-bgc\:bodyDimmed{background-color:var(--lns-color-bodyDimmed)}.xs-bgc\:background{background-color:var(--lns-color-background)}.xs-bgc\:backgroundHover{background-color:var(--lns-color-backgroundHover)}.xs-bgc\:backgroundActive{background-color:var(--lns-color-backgroundActive)}.xs-bgc\:backgroundSecondary{background-color:var(--lns-color-backgroundSecondary)}.xs-bgc\:backgroundSecondary2{background-color:var(--lns-color-backgroundSecondary2)}.xs-bgc\:overlay{background-color:var(--lns-color-overlay)}.xs-bgc\:border{background-color:var(--lns-color-border)}.xs-bgc\:focusRing{background-color:var(--lns-color-focusRing)}.xs-bgc\:record{background-color:var(--lns-color-record)}.xs-bgc\:recordHover{background-color:var(--lns-color-recordHover)}.xs-bgc\:recordActive{background-color:var(--lns-color-recordActive)}.xs-bgc\:info{background-color:var(--lns-color-info)}.xs-bgc\:success{background-color:var(--lns-color-success)}.xs-bgc\:warning{background-color:var(--lns-color-warning)}.xs-bgc\:danger{background-color:var(--lns-color-danger)}.xs-bgc\:dangerHover{background-color:var(--lns-color-dangerHover)}.xs-bgc\:dangerActive{background-color:var(--lns-color-dangerActive)}.xs-bgc\:backdrop{background-color:var(--lns-color-backdrop)}.xs-bgc\:backdropDark{background-color:var(--lns-color-backdropDark)}.xs-bgc\:backdropTwilight{background-color:var(--lns-color-backdropTwilight)}.xs-bgc\:disabledContent{background-color:var(--lns-color-disabledContent)}.xs-bgc\:highlight{background-color:var(--lns-color-highlight)}.xs-bgc\:disabledBackground{background-color:var(--lns-color-disabledBackground)}.xs-bgc\:formFieldBorder{background-color:var(--lns-color-formFieldBorder)}.xs-bgc\:formFieldBackground{background-color:var(--lns-color-formFieldBackground)}.xs-bgc\:buttonBorder{background-color:var(--lns-color-buttonBorder)}.xs-bgc\:upgrade{background-color:var(--lns-color-upgrade)}.xs-bgc\:upgradeHover{background-color:var(--lns-color-upgradeHover)}.xs-bgc\:upgradeActive{background-color:var(--lns-color-upgradeActive)}.xs-bgc\:tabBackground{background-color:var(--lns-color-tabBackground)}.xs-bgc\:discoveryBackground{background-color:var(--lns-color-discoveryBackground)}.xs-bgc\:discoveryLightBackground{background-color:var(--lns-color-discoveryLightBackground)}.xs-bgc\:discoveryTitle{background-color:var(--lns-color-discoveryTitle)}.xs-bgc\:discoveryHighlight{background-color:var(--lns-color-discoveryHighlight)}.xs-m\:0{margin:0}.xs-m\:auto{margin:auto}.xs-m\:xsmall{margin:var(--lns-space-xsmall)}.xs-m\:small{margin:var(--lns-space-small)}.xs-m\:medium{margin:var(--lns-space-medium)}.xs-m\:large{margin:var(--lns-space-large)}.xs-m\:xlarge{margin:var(--lns-space-xlarge)}.xs-m\:xxlarge{margin:var(--lns-space-xxlarge)}.xs-mt\:0{margin-top:0}.xs-mt\:auto{margin-top:auto}.xs-mt\:xsmall{margin-top:var(--lns-space-xsmall)}.xs-mt\:small{margin-top:var(--lns-space-small)}.xs-mt\:medium{margin-top:var(--lns-space-medium)}.xs-mt\:large{margin-top:var(--lns-space-large)}.xs-mt\:xlarge{margin-top:var(--lns-space-xlarge)}.xs-mt\:xxlarge{margin-top:var(--lns-space-xxlarge)}.xs-mb\:0{margin-bottom:0}.xs-mb\:auto{margin-bottom:auto}.xs-mb\:xsmall{margin-bottom:var(--lns-space-xsmall)}.xs-mb\:small{margin-bottom:var(--lns-space-small)}.xs-mb\:medium{margin-bottom:var(--lns-space-medium)}.xs-mb\:large{margin-bottom:var(--lns-space-large)}.xs-mb\:xlarge{margin-bottom:var(--lns-space-xlarge)}.xs-mb\:xxlarge{margin-bottom:var(--lns-space-xxlarge)}.xs-ml\:0{margin-left:0}.xs-ml\:auto{margin-left:auto}.xs-ml\:xsmall{margin-left:var(--lns-space-xsmall)}.xs-ml\:small{margin-left:var(--lns-space-small)}.xs-ml\:medium{margin-left:var(--lns-space-medium)}.xs-ml\:large{margin-left:var(--lns-space-large)}.xs-ml\:xlarge{margin-left:var(--lns-space-xlarge)}.xs-ml\:xxlarge{margin-left:var(--lns-space-xxlarge)}.xs-mr\:0{margin-right:0}.xs-mr\:auto{margin-right:auto}.xs-mr\:xsmall{margin-right:var(--lns-space-xsmall)}.xs-mr\:small{margin-right:var(--lns-space-small)}.xs-mr\:medium{margin-right:var(--lns-space-medium)}.xs-mr\:large{margin-right:var(--lns-space-large)}.xs-mr\:xlarge{margin-right:var(--lns-space-xlarge)}.xs-mr\:xxlarge{margin-right:var(--lns-space-xxlarge)}.xs-mx\:0{margin-left:0;margin-right:0}.xs-mx\:auto{margin-left:auto;margin-right:auto}.xs-mx\:xsmall{margin-left:var(--lns-space-xsmall);margin-right:var(--lns-space-xsmall)}.xs-mx\:small{margin-left:var(--lns-space-small);margin-right:var(--lns-space-small)}.xs-mx\:medium{margin-left:var(--lns-space-medium);margin-right:var(--lns-space-medium)}.xs-mx\:large{margin-left:var(--lns-space-large);margin-right:var(--lns-space-large)}.xs-mx\:xlarge{margin-left:var(--lns-space-xlarge);margin-right:var(--lns-space-xlarge)}.xs-mx\:xxlarge{margin-left:var(--lns-space-xxlarge);margin-right:var(--lns-space-xxlarge)}.xs-my\:0{margin-top:0;margin-bottom:0}.xs-my\:auto{margin-top:auto;margin-bottom:auto}.xs-my\:xsmall{margin-top:var(--lns-space-xsmall);margin-bottom:var(--lns-space-xsmall)}.xs-my\:small{margin-top:var(--lns-space-small);margin-bottom:var(--lns-space-small)}.xs-my\:medium{margin-top:var(--lns-space-medium);margin-bottom:var(--lns-space-medium)}.xs-my\:large{margin-top:var(--lns-space-large);margin-bottom:var(--lns-space-large)}.xs-my\:xlarge{margin-top:var(--lns-space-xlarge);margin-bottom:var(--lns-space-xlarge)}.xs-my\:xxlarge{margin-top:var(--lns-space-xxlarge);margin-bottom:var(--lns-space-xxlarge)}.xs-p\:0{padding:0}.xs-p\:xsmall{padding:var(--lns-space-xsmall)}.xs-p\:small{padding:var(--lns-space-small)}.xs-p\:medium{padding:var(--lns-space-medium)}.xs-p\:large{padding:var(--lns-space-large)}.xs-p\:xlarge{padding:var(--lns-space-xlarge)}.xs-p\:xxlarge{padding:var(--lns-space-xxlarge)}.xs-pt\:0{padding-top:0}.xs-pt\:xsmall{padding-top:var(--lns-space-xsmall)}.xs-pt\:small{padding-top:var(--lns-space-small)}.xs-pt\:medium{padding-top:var(--lns-space-medium)}.xs-pt\:large{padding-top:var(--lns-space-large)}.xs-pt\:xlarge{padding-top:var(--lns-space-xlarge)}.xs-pt\:xxlarge{padding-top:var(--lns-space-xxlarge)}.xs-pb\:0{padding-bottom:0}.xs-pb\:xsmall{padding-bottom:var(--lns-space-xsmall)}.xs-pb\:small{padding-bottom:var(--lns-space-small)}.xs-pb\:medium{padding-bottom:var(--lns-space-medium)}.xs-pb\:large{padding-bottom:var(--lns-space-large)}.xs-pb\:xlarge{padding-bottom:var(--lns-space-xlarge)}.xs-pb\:xxlarge{padding-bottom:var(--lns-space-xxlarge)}.xs-pl\:0{padding-left:0}.xs-pl\:xsmall{padding-left:var(--lns-space-xsmall)}.xs-pl\:small{padding-left:var(--lns-space-small)}.xs-pl\:medium{padding-left:var(--lns-space-medium)}.xs-pl\:large{padding-left:var(--lns-space-large)}.xs-pl\:xlarge{padding-left:var(--lns-space-xlarge)}.xs-pl\:xxlarge{padding-left:var(--lns-space-xxlarge)}.xs-pr\:0{padding-right:0}.xs-pr\:xsmall{padding-right:var(--lns-space-xsmall)}.xs-pr\:small{padding-right:var(--lns-space-small)}.xs-pr\:medium{padding-right:var(--lns-space-medium)}.xs-pr\:large{padding-right:var(--lns-space-large)}.xs-pr\:xlarge{padding-right:var(--lns-space-xlarge)}.xs-pr\:xxlarge{padding-right:var(--lns-space-xxlarge)}.xs-px\:0{padding-left:0;padding-right:0}.xs-px\:xsmall{padding-left:var(--lns-space-xsmall);padding-right:var(--lns-space-xsmall)}.xs-px\:small{padding-left:var(--lns-space-small);padding-right:var(--lns-space-small)}.xs-px\:medium{padding-left:var(--lns-space-medium);padding-right:var(--lns-space-medium)}.xs-px\:large{padding-left:var(--lns-space-large);padding-right:var(--lns-space-large)}.xs-px\:xlarge{padding-left:var(--lns-space-xlarge);padding-right:var(--lns-space-xlarge)}.xs-px\:xxlarge{padding-left:var(--lns-space-xxlarge);padding-right:var(--lns-space-xxlarge)}.xs-py\:0{padding-top:0;padding-bottom:0}.xs-py\:xsmall{padding-top:var(--lns-space-xsmall);padding-bottom:var(--lns-space-xsmall)}.xs-py\:small{padding-top:var(--lns-space-small);padding-bottom:var(--lns-space-small)}.xs-py\:medium{padding-top:var(--lns-space-medium);padding-bottom:var(--lns-space-medium)}.xs-py\:large{padding-top:var(--lns-space-large);padding-bottom:var(--lns-space-large)}.xs-py\:xlarge{padding-top:var(--lns-space-xlarge);padding-bottom:var(--lns-space-xlarge)}.xs-py\:xxlarge{padding-top:var(--lns-space-xxlarge);padding-bottom:var(--lns-space-xxlarge)}.xs-text\:small{font-size:var(--lns-fontSize-small);line-height:var(--lns-lineHeight-small)}.xs-text\:body-sm{font-size:var(--lns-fontSize-body-sm);line-height:var(--lns-lineHeight-body-sm)}.xs-text\:medium{font-size:var(--lns-fontSize-medium);line-height:var(--lns-lineHeight-medium)}.xs-text\:body-md{font-size:var(--lns-fontSize-body-md);line-height:var(--lns-lineHeight-body-md)}.xs-text\:large{font-size:var(--lns-fontSize-large);line-height:var(--lns-lineHeight-large)}.xs-text\:body-lg{font-size:var(--lns-fontSize-body-lg);line-height:var(--lns-lineHeight-body-lg)}.xs-text\:xlarge{font-size:var(--lns-fontSize-xlarge);line-height:var(--lns-lineHeight-xlarge)}.xs-text\:heading-sm{font-size:var(--lns-fontSize-heading-sm);line-height:var(--lns-lineHeight-heading-sm)}.xs-text\:xxlarge{font-size:var(--lns-fontSize-xxlarge);line-height:var(--lns-lineHeight-xxlarge)}.xs-text\:heading-md{font-size:var(--lns-fontSize-heading-md);line-height:var(--lns-lineHeight-heading-md)}.xs-text\:xxxlarge{font-size:var(--lns-fontSize-xxxlarge);line-height:var(--lns-lineHeight-xxxlarge)}.xs-text\:heading-lg{font-size:var(--lns-fontSize-heading-lg);line-height:var(--lns-lineHeight-heading-lg)}.xs-weight\:book{font-weight:var(--lns-fontWeight-book)}.xs-weight\:bold{font-weight:var(--lns-fontWeight-bold)}.xs-text\:body{font-size:var(--lns-fontSize-body-md);line-height:var(--lns-lineHeight-body-md);font-weight:var(--lns-fontWeight-book)}.xs-text\:title{font-size:var(--lns-fontSize-body-lg);line-height:var(--lns-lineHeight-body-lg);font-weight:var(--lns-fontWeight-bold)}.xs-text\:mainTitle{font-size:var(--lns-fontSize-heading-md);line-height:var(--lns-lineHeight-heading-md);font-weight:var(--lns-fontWeight-bold)}.xs-text\:left{text-align:left}.xs-text\:right{text-align:right}.xs-text\:center{text-align:center}.xs-border{border:1px solid var(--lns-color-border)}.xs-borderTop{border-top:1px solid var(--lns-color-border)}.xs-borderBottom{border-bottom:1px solid var(--lns-color-border)}.xs-borderLeft{border-left:1px solid var(--lns-color-border)}.xs-borderRight{border-right:1px solid var(--lns-color-border)}.xs-inline{display:inline}.xs-block{display:block}.xs-flex{display:flex}.xs-inlineBlock{display:inline-block}.xs-inlineFlex{display:inline-flex}.xs-none{display:none}.xs-flexWrap{flex-wrap:wrap}.xs-flexDirection\:column{flex-direction:column}.xs-flexDirection\:row{flex-direction:row}.xs-items\:stretch{align-items:stretch}.xs-items\:center{align-items:center}.xs-items\:baseline{align-items:baseline}.xs-items\:flexStart{align-items:flex-start}.xs-items\:flexEnd{align-items:flex-end}.xs-items\:selfStart{align-items:self-start}.xs-items\:selfEnd{align-items:self-end}.xs-justify\:flexStart{justify-content:flex-start}.xs-justify\:flexEnd{justify-content:flex-end}.xs-justify\:center{justify-content:center}.xs-justify\:spaceBetween{justify-content:space-between}.xs-justify\:spaceAround{justify-content:space-around}.xs-justify\:spaceEvenly{justify-content:space-evenly}.xs-grow\:0{flex-grow:0}.xs-grow\:1{flex-grow:1}.xs-shrink\:0{flex-shrink:0}.xs-shrink\:1{flex-shrink:1}.xs-self\:auto{align-self:auto}.xs-self\:flexStart{align-self:flex-start}.xs-self\:flexEnd{align-self:flex-end}.xs-self\:center{align-self:center}.xs-self\:baseline{align-self:baseline}.xs-self\:stretch{align-self:stretch}.xs-overflow\:hidden{overflow:hidden}.xs-overflow\:auto{overflow:auto}.xs-relative{position:relative}.xs-absolute{position:absolute}.xs-sticky{position:sticky}.xs-fixed{position:fixed}.xs-top\:0{top:0}.xs-top\:auto{top:auto}.xs-top\:xsmall{top:var(--lns-space-xsmall)}.xs-top\:small{top:var(--lns-space-small)}.xs-top\:medium{top:var(--lns-space-medium)}.xs-top\:large{top:var(--lns-space-large)}.xs-top\:xlarge{top:var(--lns-space-xlarge)}.xs-top\:xxlarge{top:var(--lns-space-xxlarge)}.xs-bottom\:0{bottom:0}.xs-bottom\:auto{bottom:auto}.xs-bottom\:xsmall{bottom:var(--lns-space-xsmall)}.xs-bottom\:small{bottom:var(--lns-space-small)}.xs-bottom\:medium{bottom:var(--lns-space-medium)}.xs-bottom\:large{bottom:var(--lns-space-large)}.xs-bottom\:xlarge{bottom:var(--lns-space-xlarge)}.xs-bottom\:xxlarge{bottom:var(--lns-space-xxlarge)}.xs-left\:0{left:0}.xs-left\:auto{left:auto}.xs-left\:xsmall{left:var(--lns-space-xsmall)}.xs-left\:small{left:var(--lns-space-small)}.xs-left\:medium{left:var(--lns-space-medium)}.xs-left\:large{left:var(--lns-space-large)}.xs-left\:xlarge{left:var(--lns-space-xlarge)}.xs-left\:xxlarge{left:var(--lns-space-xxlarge)}.xs-right\:0{right:0}.xs-right\:auto{right:auto}.xs-right\:xsmall{right:var(--lns-space-xsmall)}.xs-right\:small{right:var(--lns-space-small)}.xs-right\:medium{right:var(--lns-space-medium)}.xs-right\:large{right:var(--lns-space-large)}.xs-right\:xlarge{right:var(--lns-space-xlarge)}.xs-right\:xxlarge{right:var(--lns-space-xxlarge)}.xs-width\:auto{width:auto}.xs-width\:full{width:100%}.xs-width\:0{width:0}.xs-minWidth\:0{min-width:0}.xs-height\:auto{height:auto}.xs-height\:full{height:100%}.xs-height\:0{height:0}.xs-ellipsis{overflow:hidden;text-overflow:ellipsis;white-space:nowrap}.xs-srOnly{position:absolute;width:1px;height:1px;padding:0;margin:-1px;overflow:hidden;clip:rect(0, 0, 0, 0);white-space:nowrap;border-width:0}}@media(min-width:48em){.sm-c\:red{color:var(--lns-color-red)}.sm-c\:blurpleLight{color:var(--lns-color-blurpleLight)}.sm-c\:blurpleMedium{color:var(--lns-color-blurpleMedium)}.sm-c\:blurple{color:var(--lns-color-blurple)}.sm-c\:blurpleDark{color:var(--lns-color-blurpleDark)}.sm-c\:offWhite{color:var(--lns-color-offWhite)}.sm-c\:blueLight{color:var(--lns-color-blueLight)}.sm-c\:blue{color:var(--lns-color-blue)}.sm-c\:blueDark{color:var(--lns-color-blueDark)}.sm-c\:orangeLight{color:var(--lns-color-orangeLight)}.sm-c\:orange{color:var(--lns-color-orange)}.sm-c\:orangeDark{color:var(--lns-color-orangeDark)}.sm-c\:tealLight{color:var(--lns-color-tealLight)}.sm-c\:teal{color:var(--lns-color-teal)}.sm-c\:tealDark{color:var(--lns-color-tealDark)}.sm-c\:yellowLight{color:var(--lns-color-yellowLight)}.sm-c\:yellow{color:var(--lns-color-yellow)}.sm-c\:yellowDark{color:var(--lns-color-yellowDark)}.sm-c\:grey8{color:var(--lns-color-grey8)}.sm-c\:grey7{color:var(--lns-color-grey7)}.sm-c\:grey6{color:var(--lns-color-grey6)}.sm-c\:grey5{color:var(--lns-color-grey5)}.sm-c\:grey4{color:var(--lns-color-grey4)}.sm-c\:grey3{color:var(--lns-color-grey3)}.sm-c\:grey2{color:var(--lns-color-grey2)}.sm-c\:grey1{color:var(--lns-color-grey1)}.sm-c\:white{color:var(--lns-color-white)}.sm-c\:primary{color:var(--lns-color-primary)}.sm-c\:primaryHover{color:var(--lns-color-primaryHover)}.sm-c\:primaryActive{color:var(--lns-color-primaryActive)}.sm-c\:body{color:var(--lns-color-body)}.sm-c\:bodyDimmed{color:var(--lns-color-bodyDimmed)}.sm-c\:background{color:var(--lns-color-background)}.sm-c\:backgroundHover{color:var(--lns-color-backgroundHover)}.sm-c\:backgroundActive{color:var(--lns-color-backgroundActive)}.sm-c\:backgroundSecondary{color:var(--lns-color-backgroundSecondary)}.sm-c\:backgroundSecondary2{color:var(--lns-color-backgroundSecondary2)}.sm-c\:overlay{color:var(--lns-color-overlay)}.sm-c\:border{color:var(--lns-color-border)}.sm-c\:focusRing{color:var(--lns-color-focusRing)}.sm-c\:record{color:var(--lns-color-record)}.sm-c\:recordHover{color:var(--lns-color-recordHover)}.sm-c\:recordActive{color:var(--lns-color-recordActive)}.sm-c\:info{color:var(--lns-color-info)}.sm-c\:success{color:var(--lns-color-success)}.sm-c\:warning{color:var(--lns-color-warning)}.sm-c\:danger{color:var(--lns-color-danger)}.sm-c\:dangerHover{color:var(--lns-color-dangerHover)}.sm-c\:dangerActive{color:var(--lns-color-dangerActive)}.sm-c\:backdrop{color:var(--lns-color-backdrop)}.sm-c\:backdropDark{color:var(--lns-color-backdropDark)}.sm-c\:backdropTwilight{color:var(--lns-color-backdropTwilight)}.sm-c\:disabledContent{color:var(--lns-color-disabledContent)}.sm-c\:highlight{color:var(--lns-color-highlight)}.sm-c\:disabledBackground{color:var(--lns-color-disabledBackground)}.sm-c\:formFieldBorder{color:var(--lns-color-formFieldBorder)}.sm-c\:formFieldBackground{color:var(--lns-color-formFieldBackground)}.sm-c\:buttonBorder{color:var(--lns-color-buttonBorder)}.sm-c\:upgrade{color:var(--lns-color-upgrade)}.sm-c\:upgradeHover{color:var(--lns-color-upgradeHover)}.sm-c\:upgradeActive{color:var(--lns-color-upgradeActive)}.sm-c\:tabBackground{color:var(--lns-color-tabBackground)}.sm-c\:discoveryBackground{color:var(--lns-color-discoveryBackground)}.sm-c\:discoveryLightBackground{color:var(--lns-color-discoveryLightBackground)}.sm-c\:discoveryTitle{color:var(--lns-color-discoveryTitle)}.sm-c\:discoveryHighlight{color:var(--lns-color-discoveryHighlight)}.sm-shadow\:small{box-shadow:var(--lns-shadow-small)}.sm-shadow\:medium{box-shadow:var(--lns-shadow-medium)}.sm-shadow\:large{box-shadow:var(--lns-shadow-large)}.sm-radius\:medium{border-radius:var(--lns-radius-medium)}.sm-radius\:large{border-radius:var(--lns-radius-large)}.sm-radius\:xlarge{border-radius:var(--lns-radius-xlarge)}.sm-radius\:full{border-radius:var(--lns-radius-full)}.sm-bgc\:red{background-color:var(--lns-color-red)}.sm-bgc\:blurpleLight{background-color:var(--lns-color-blurpleLight)}.sm-bgc\:blurpleMedium{background-color:var(--lns-color-blurpleMedium)}.sm-bgc\:blurple{background-color:var(--lns-color-blurple)}.sm-bgc\:blurpleDark{background-color:var(--lns-color-blurpleDark)}.sm-bgc\:offWhite{background-color:var(--lns-color-offWhite)}.sm-bgc\:blueLight{background-color:var(--lns-color-blueLight)}.sm-bgc\:blue{background-color:var(--lns-color-blue)}.sm-bgc\:blueDark{background-color:var(--lns-color-blueDark)}.sm-bgc\:orangeLight{background-color:var(--lns-color-orangeLight)}.sm-bgc\:orange{background-color:var(--lns-color-orange)}.sm-bgc\:orangeDark{background-color:var(--lns-color-orangeDark)}.sm-bgc\:tealLight{background-color:var(--lns-color-tealLight)}.sm-bgc\:teal{background-color:var(--lns-color-teal)}.sm-bgc\:tealDark{background-color:var(--lns-color-tealDark)}.sm-bgc\:yellowLight{background-color:var(--lns-color-yellowLight)}.sm-bgc\:yellow{background-color:var(--lns-color-yellow)}.sm-bgc\:yellowDark{background-color:var(--lns-color-yellowDark)}.sm-bgc\:grey8{background-color:var(--lns-color-grey8)}.sm-bgc\:grey7{background-color:var(--lns-color-grey7)}.sm-bgc\:grey6{background-color:var(--lns-color-grey6)}.sm-bgc\:grey5{background-color:var(--lns-color-grey5)}.sm-bgc\:grey4{background-color:var(--lns-color-grey4)}.sm-bgc\:grey3{background-color:var(--lns-color-grey3)}.sm-bgc\:grey2{background-color:var(--lns-color-grey2)}.sm-bgc\:grey1{background-color:var(--lns-color-grey1)}.sm-bgc\:white{background-color:var(--lns-color-white)}.sm-bgc\:primary{background-color:var(--lns-color-primary)}.sm-bgc\:primaryHover{background-color:var(--lns-color-primaryHover)}.sm-bgc\:primaryActive{background-color:var(--lns-color-primaryActive)}.sm-bgc\:body{background-color:var(--lns-color-body)}.sm-bgc\:bodyDimmed{background-color:var(--lns-color-bodyDimmed)}.sm-bgc\:background{background-color:var(--lns-color-background)}.sm-bgc\:backgroundHover{background-color:var(--lns-color-backgroundHover)}.sm-bgc\:backgroundActive{background-color:var(--lns-color-backgroundActive)}.sm-bgc\:backgroundSecondary{background-color:var(--lns-color-backgroundSecondary)}.sm-bgc\:backgroundSecondary2{background-color:var(--lns-color-backgroundSecondary2)}.sm-bgc\:overlay{background-color:var(--lns-color-overlay)}.sm-bgc\:border{background-color:var(--lns-color-border)}.sm-bgc\:focusRing{background-color:var(--lns-color-focusRing)}.sm-bgc\:record{background-color:var(--lns-color-record)}.sm-bgc\:recordHover{background-color:var(--lns-color-recordHover)}.sm-bgc\:recordActive{background-color:var(--lns-color-recordActive)}.sm-bgc\:info{background-color:var(--lns-color-info)}.sm-bgc\:success{background-color:var(--lns-color-success)}.sm-bgc\:warning{background-color:var(--lns-color-warning)}.sm-bgc\:danger{background-color:var(--lns-color-danger)}.sm-bgc\:dangerHover{background-color:var(--lns-color-dangerHover)}.sm-bgc\:dangerActive{background-color:var(--lns-color-dangerActive)}.sm-bgc\:backdrop{background-color:var(--lns-color-backdrop)}.sm-bgc\:backdropDark{background-color:var(--lns-color-backdropDark)}.sm-bgc\:backdropTwilight{background-color:var(--lns-color-backdropTwilight)}.sm-bgc\:disabledContent{background-color:var(--lns-color-disabledContent)}.sm-bgc\:highlight{background-color:var(--lns-color-highlight)}.sm-bgc\:disabledBackground{background-color:var(--lns-color-disabledBackground)}.sm-bgc\:formFieldBorder{background-color:var(--lns-color-formFieldBorder)}.sm-bgc\:formFieldBackground{background-color:var(--lns-color-formFieldBackground)}.sm-bgc\:buttonBorder{background-color:var(--lns-color-buttonBorder)}.sm-bgc\:upgrade{background-color:var(--lns-color-upgrade)}.sm-bgc\:upgradeHover{background-color:var(--lns-color-upgradeHover)}.sm-bgc\:upgradeActive{background-color:var(--lns-color-upgradeActive)}.sm-bgc\:tabBackground{background-color:var(--lns-color-tabBackground)}.sm-bgc\:discoveryBackground{background-color:var(--lns-color-discoveryBackground)}.sm-bgc\:discoveryLightBackground{background-color:var(--lns-color-discoveryLightBackground)}.sm-bgc\:discoveryTitle{background-color:var(--lns-color-discoveryTitle)}.sm-bgc\:discoveryHighlight{background-color:var(--lns-color-discoveryHighlight)}.sm-m\:0{margin:0}.sm-m\:auto{margin:auto}.sm-m\:xsmall{margin:var(--lns-space-xsmall)}.sm-m\:small{margin:var(--lns-space-small)}.sm-m\:medium{margin:var(--lns-space-medium)}.sm-m\:large{margin:var(--lns-space-large)}.sm-m\:xlarge{margin:var(--lns-space-xlarge)}.sm-m\:xxlarge{margin:var(--lns-space-xxlarge)}.sm-mt\:0{margin-top:0}.sm-mt\:auto{margin-top:auto}.sm-mt\:xsmall{margin-top:var(--lns-space-xsmall)}.sm-mt\:small{margin-top:var(--lns-space-small)}.sm-mt\:medium{margin-top:var(--lns-space-medium)}.sm-mt\:large{margin-top:var(--lns-space-large)}.sm-mt\:xlarge{margin-top:var(--lns-space-xlarge)}.sm-mt\:xxlarge{margin-top:var(--lns-space-xxlarge)}.sm-mb\:0{margin-bottom:0}.sm-mb\:auto{margin-bottom:auto}.sm-mb\:xsmall{margin-bottom:var(--lns-space-xsmall)}.sm-mb\:small{margin-bottom:var(--lns-space-small)}.sm-mb\:medium{margin-bottom:var(--lns-space-medium)}.sm-mb\:large{margin-bottom:var(--lns-space-large)}.sm-mb\:xlarge{margin-bottom:var(--lns-space-xlarge)}.sm-mb\:xxlarge{margin-bottom:var(--lns-space-xxlarge)}.sm-ml\:0{margin-left:0}.sm-ml\:auto{margin-left:auto}.sm-ml\:xsmall{margin-left:var(--lns-space-xsmall)}.sm-ml\:small{margin-left:var(--lns-space-small)}.sm-ml\:medium{margin-left:var(--lns-space-medium)}.sm-ml\:large{margin-left:var(--lns-space-large)}.sm-ml\:xlarge{margin-left:var(--lns-space-xlarge)}.sm-ml\:xxlarge{margin-left:var(--lns-space-xxlarge)}.sm-mr\:0{margin-right:0}.sm-mr\:auto{margin-right:auto}.sm-mr\:xsmall{margin-right:var(--lns-space-xsmall)}.sm-mr\:small{margin-right:var(--lns-space-small)}.sm-mr\:medium{margin-right:var(--lns-space-medium)}.sm-mr\:large{margin-right:var(--lns-space-large)}.sm-mr\:xlarge{margin-right:var(--lns-space-xlarge)}.sm-mr\:xxlarge{margin-right:var(--lns-space-xxlarge)}.sm-mx\:0{margin-left:0;margin-right:0}.sm-mx\:auto{margin-left:auto;margin-right:auto}.sm-mx\:xsmall{margin-left:var(--lns-space-xsmall);margin-right:var(--lns-space-xsmall)}.sm-mx\:small{margin-left:var(--lns-space-small);margin-right:var(--lns-space-small)}.sm-mx\:medium{margin-left:var(--lns-space-medium);margin-right:var(--lns-space-medium)}.sm-mx\:large{margin-left:var(--lns-space-large);margin-right:var(--lns-space-large)}.sm-mx\:xlarge{margin-left:var(--lns-space-xlarge);margin-right:var(--lns-space-xlarge)}.sm-mx\:xxlarge{margin-left:var(--lns-space-xxlarge);margin-right:var(--lns-space-xxlarge)}.sm-my\:0{margin-top:0;margin-bottom:0}.sm-my\:auto{margin-top:auto;margin-bottom:auto}.sm-my\:xsmall{margin-top:var(--lns-space-xsmall);margin-bottom:var(--lns-space-xsmall)}.sm-my\:small{margin-top:var(--lns-space-small);margin-bottom:var(--lns-space-small)}.sm-my\:medium{margin-top:var(--lns-space-medium);margin-bottom:var(--lns-space-medium)}.sm-my\:large{margin-top:var(--lns-space-large);margin-bottom:var(--lns-space-large)}.sm-my\:xlarge{margin-top:var(--lns-space-xlarge);margin-bottom:var(--lns-space-xlarge)}.sm-my\:xxlarge{margin-top:var(--lns-space-xxlarge);margin-bottom:var(--lns-space-xxlarge)}.sm-p\:0{padding:0}.sm-p\:xsmall{padding:var(--lns-space-xsmall)}.sm-p\:small{padding:var(--lns-space-small)}.sm-p\:medium{padding:var(--lns-space-medium)}.sm-p\:large{padding:var(--lns-space-large)}.sm-p\:xlarge{padding:var(--lns-space-xlarge)}.sm-p\:xxlarge{padding:var(--lns-space-xxlarge)}.sm-pt\:0{padding-top:0}.sm-pt\:xsmall{padding-top:var(--lns-space-xsmall)}.sm-pt\:small{padding-top:var(--lns-space-small)}.sm-pt\:medium{padding-top:var(--lns-space-medium)}.sm-pt\:large{padding-top:var(--lns-space-large)}.sm-pt\:xlarge{padding-top:var(--lns-space-xlarge)}.sm-pt\:xxlarge{padding-top:var(--lns-space-xxlarge)}.sm-pb\:0{padding-bottom:0}.sm-pb\:xsmall{padding-bottom:var(--lns-space-xsmall)}.sm-pb\:small{padding-bottom:var(--lns-space-small)}.sm-pb\:medium{padding-bottom:var(--lns-space-medium)}.sm-pb\:large{padding-bottom:var(--lns-space-large)}.sm-pb\:xlarge{padding-bottom:var(--lns-space-xlarge)}.sm-pb\:xxlarge{padding-bottom:var(--lns-space-xxlarge)}.sm-pl\:0{padding-left:0}.sm-pl\:xsmall{padding-left:var(--lns-space-xsmall)}.sm-pl\:small{padding-left:var(--lns-space-small)}.sm-pl\:medium{padding-left:var(--lns-space-medium)}.sm-pl\:large{padding-left:var(--lns-space-large)}.sm-pl\:xlarge{padding-left:var(--lns-space-xlarge)}.sm-pl\:xxlarge{padding-left:var(--lns-space-xxlarge)}.sm-pr\:0{padding-right:0}.sm-pr\:xsmall{padding-right:var(--lns-space-xsmall)}.sm-pr\:small{padding-right:var(--lns-space-small)}.sm-pr\:medium{padding-right:var(--lns-space-medium)}.sm-pr\:large{padding-right:var(--lns-space-large)}.sm-pr\:xlarge{padding-right:var(--lns-space-xlarge)}.sm-pr\:xxlarge{padding-right:var(--lns-space-xxlarge)}.sm-px\:0{padding-left:0;padding-right:0}.sm-px\:xsmall{padding-left:var(--lns-space-xsmall);padding-right:var(--lns-space-xsmall)}.sm-px\:small{padding-left:var(--lns-space-small);padding-right:var(--lns-space-small)}.sm-px\:medium{padding-left:var(--lns-space-medium);padding-right:var(--lns-space-medium)}.sm-px\:large{padding-left:var(--lns-space-large);padding-right:var(--lns-space-large)}.sm-px\:xlarge{padding-left:var(--lns-space-xlarge);padding-right:var(--lns-space-xlarge)}.sm-px\:xxlarge{padding-left:var(--lns-space-xxlarge);padding-right:var(--lns-space-xxlarge)}.sm-py\:0{padding-top:0;padding-bottom:0}.sm-py\:xsmall{padding-top:var(--lns-space-xsmall);padding-bottom:var(--lns-space-xsmall)}.sm-py\:small{padding-top:var(--lns-space-small);padding-bottom:var(--lns-space-small)}.sm-py\:medium{padding-top:var(--lns-space-medium);padding-bottom:var(--lns-space-medium)}.sm-py\:large{padding-top:var(--lns-space-large);padding-bottom:var(--lns-space-large)}.sm-py\:xlarge{padding-top:var(--lns-space-xlarge);padding-bottom:var(--lns-space-xlarge)}.sm-py\:xxlarge{padding-top:var(--lns-space-xxlarge);padding-bottom:var(--lns-space-xxlarge)}.sm-text\:small{font-size:var(--lns-fontSize-small);line-height:var(--lns-lineHeight-small)}.sm-text\:body-sm{font-size:var(--lns-fontSize-body-sm);line-height:var(--lns-lineHeight-body-sm)}.sm-text\:medium{font-size:var(--lns-fontSize-medium);line-height:var(--lns-lineHeight-medium)}.sm-text\:body-md{font-size:var(--lns-fontSize-body-md);line-height:var(--lns-lineHeight-body-md)}.sm-text\:large{font-size:var(--lns-fontSize-large);line-height:var(--lns-lineHeight-large)}.sm-text\:body-lg{font-size:var(--lns-fontSize-body-lg);line-height:var(--lns-lineHeight-body-lg)}.sm-text\:xlarge{font-size:var(--lns-fontSize-xlarge);line-height:var(--lns-lineHeight-xlarge)}.sm-text\:heading-sm{font-size:var(--lns-fontSize-heading-sm);line-height:var(--lns-lineHeight-heading-sm)}.sm-text\:xxlarge{font-size:var(--lns-fontSize-xxlarge);line-height:var(--lns-lineHeight-xxlarge)}.sm-text\:heading-md{font-size:var(--lns-fontSize-heading-md);line-height:var(--lns-lineHeight-heading-md)}.sm-text\:xxxlarge{font-size:var(--lns-fontSize-xxxlarge);line-height:var(--lns-lineHeight-xxxlarge)}.sm-text\:heading-lg{font-size:var(--lns-fontSize-heading-lg);line-height:var(--lns-lineHeight-heading-lg)}.sm-weight\:book{font-weight:var(--lns-fontWeight-book)}.sm-weight\:bold{font-weight:var(--lns-fontWeight-bold)}.sm-text\:body{font-size:var(--lns-fontSize-body-md);line-height:var(--lns-lineHeight-body-md);font-weight:var(--lns-fontWeight-book)}.sm-text\:title{font-size:var(--lns-fontSize-body-lg);line-height:var(--lns-lineHeight-body-lg);font-weight:var(--lns-fontWeight-bold)}.sm-text\:mainTitle{font-size:var(--lns-fontSize-heading-md);line-height:var(--lns-lineHeight-heading-md);font-weight:var(--lns-fontWeight-bold)}.sm-text\:left{text-align:left}.sm-text\:right{text-align:right}.sm-text\:center{text-align:center}.sm-border{border:1px solid var(--lns-color-border)}.sm-borderTop{border-top:1px solid var(--lns-color-border)}.sm-borderBottom{border-bottom:1px solid var(--lns-color-border)}.sm-borderLeft{border-left:1px solid var(--lns-color-border)}.sm-borderRight{border-right:1px solid var(--lns-color-border)}.sm-inline{display:inline}.sm-block{display:block}.sm-flex{display:flex}.sm-inlineBlock{display:inline-block}.sm-inlineFlex{display:inline-flex}.sm-none{display:none}.sm-flexWrap{flex-wrap:wrap}.sm-flexDirection\:column{flex-direction:column}.sm-flexDirection\:row{flex-direction:row}.sm-items\:stretch{align-items:stretch}.sm-items\:center{align-items:center}.sm-items\:baseline{align-items:baseline}.sm-items\:flexStart{align-items:flex-start}.sm-items\:flexEnd{align-items:flex-end}.sm-items\:selfStart{align-items:self-start}.sm-items\:selfEnd{align-items:self-end}.sm-justify\:flexStart{justify-content:flex-start}.sm-justify\:flexEnd{justify-content:flex-end}.sm-justify\:center{justify-content:center}.sm-justify\:spaceBetween{justify-content:space-between}.sm-justify\:spaceAround{justify-content:space-around}.sm-justify\:spaceEvenly{justify-content:space-evenly}.sm-grow\:0{flex-grow:0}.sm-grow\:1{flex-grow:1}.sm-shrink\:0{flex-shrink:0}.sm-shrink\:1{flex-shrink:1}.sm-self\:auto{align-self:auto}.sm-self\:flexStart{align-self:flex-start}.sm-self\:flexEnd{align-self:flex-end}.sm-self\:center{align-self:center}.sm-self\:baseline{align-self:baseline}.sm-self\:stretch{align-self:stretch}.sm-overflow\:hidden{overflow:hidden}.sm-overflow\:auto{overflow:auto}.sm-relative{position:relative}.sm-absolute{position:absolute}.sm-sticky{position:sticky}.sm-fixed{position:fixed}.sm-top\:0{top:0}.sm-top\:auto{top:auto}.sm-top\:xsmall{top:var(--lns-space-xsmall)}.sm-top\:small{top:var(--lns-space-small)}.sm-top\:medium{top:var(--lns-space-medium)}.sm-top\:large{top:var(--lns-space-large)}.sm-top\:xlarge{top:var(--lns-space-xlarge)}.sm-top\:xxlarge{top:var(--lns-space-xxlarge)}.sm-bottom\:0{bottom:0}.sm-bottom\:auto{bottom:auto}.sm-bottom\:xsmall{bottom:var(--lns-space-xsmall)}.sm-bottom\:small{bottom:var(--lns-space-small)}.sm-bottom\:medium{bottom:var(--lns-space-medium)}.sm-bottom\:large{bottom:var(--lns-space-large)}.sm-bottom\:xlarge{bottom:var(--lns-space-xlarge)}.sm-bottom\:xxlarge{bottom:var(--lns-space-xxlarge)}.sm-left\:0{left:0}.sm-left\:auto{left:auto}.sm-left\:xsmall{left:var(--lns-space-xsmall)}.sm-left\:small{left:var(--lns-space-small)}.sm-left\:medium{left:var(--lns-space-medium)}.sm-left\:large{left:var(--lns-space-large)}.sm-left\:xlarge{left:var(--lns-space-xlarge)}.sm-left\:xxlarge{left:var(--lns-space-xxlarge)}.sm-right\:0{right:0}.sm-right\:auto{right:auto}.sm-right\:xsmall{right:var(--lns-space-xsmall)}.sm-right\:small{right:var(--lns-space-small)}.sm-right\:medium{right:var(--lns-space-medium)}.sm-right\:large{right:var(--lns-space-large)}.sm-right\:xlarge{right:var(--lns-space-xlarge)}.sm-right\:xxlarge{right:var(--lns-space-xxlarge)}.sm-width\:auto{width:auto}.sm-width\:full{width:100%}.sm-width\:0{width:0}.sm-minWidth\:0{min-width:0}.sm-height\:auto{height:auto}.sm-height\:full{height:100%}.sm-height\:0{height:0}.sm-ellipsis{overflow:hidden;text-overflow:ellipsis;white-space:nowrap}.sm-srOnly{position:absolute;width:1px;height:1px;padding:0;margin:-1px;overflow:hidden;clip:rect(0, 0, 0, 0);white-space:nowrap;border-width:0}}@media(min-width:64em){.md-c\:red{color:var(--lns-color-red)}.md-c\:blurpleLight{color:var(--lns-color-blurpleLight)}.md-c\:blurpleMedium{color:var(--lns-color-blurpleMedium)}.md-c\:blurple{color:var(--lns-color-blurple)}.md-c\:blurpleDark{color:var(--lns-color-blurpleDark)}.md-c\:offWhite{color:var(--lns-color-offWhite)}.md-c\:blueLight{color:var(--lns-color-blueLight)}.md-c\:blue{color:var(--lns-color-blue)}.md-c\:blueDark{color:var(--lns-color-blueDark)}.md-c\:orangeLight{color:var(--lns-color-orangeLight)}.md-c\:orange{color:var(--lns-color-orange)}.md-c\:orangeDark{color:var(--lns-color-orangeDark)}.md-c\:tealLight{color:var(--lns-color-tealLight)}.md-c\:teal{color:var(--lns-color-teal)}.md-c\:tealDark{color:var(--lns-color-tealDark)}.md-c\:yellowLight{color:var(--lns-color-yellowLight)}.md-c\:yellow{color:var(--lns-color-yellow)}.md-c\:yellowDark{color:var(--lns-color-yellowDark)}.md-c\:grey8{color:var(--lns-color-grey8)}.md-c\:grey7{color:var(--lns-color-grey7)}.md-c\:grey6{color:var(--lns-color-grey6)}.md-c\:grey5{color:var(--lns-color-grey5)}.md-c\:grey4{color:var(--lns-color-grey4)}.md-c\:grey3{color:var(--lns-color-grey3)}.md-c\:grey2{color:var(--lns-color-grey2)}.md-c\:grey1{color:var(--lns-color-grey1)}.md-c\:white{color:var(--lns-color-white)}.md-c\:primary{color:var(--lns-color-primary)}.md-c\:primaryHover{color:var(--lns-color-primaryHover)}.md-c\:primaryActive{color:var(--lns-color-primaryActive)}.md-c\:body{color:var(--lns-color-body)}.md-c\:bodyDimmed{color:var(--lns-color-bodyDimmed)}.md-c\:background{color:var(--lns-color-background)}.md-c\:backgroundHover{color:var(--lns-color-backgroundHover)}.md-c\:backgroundActive{color:var(--lns-color-backgroundActive)}.md-c\:backgroundSecondary{color:var(--lns-color-backgroundSecondary)}.md-c\:backgroundSecondary2{color:var(--lns-color-backgroundSecondary2)}.md-c\:overlay{color:var(--lns-color-overlay)}.md-c\:border{color:var(--lns-color-border)}.md-c\:focusRing{color:var(--lns-color-focusRing)}.md-c\:record{color:var(--lns-color-record)}.md-c\:recordHover{color:var(--lns-color-recordHover)}.md-c\:recordActive{color:var(--lns-color-recordActive)}.md-c\:info{color:var(--lns-color-info)}.md-c\:success{color:var(--lns-color-success)}.md-c\:warning{color:var(--lns-color-warning)}.md-c\:danger{color:var(--lns-color-danger)}.md-c\:dangerHover{color:var(--lns-color-dangerHover)}.md-c\:dangerActive{color:var(--lns-color-dangerActive)}.md-c\:backdrop{color:var(--lns-color-backdrop)}.md-c\:backdropDark{color:var(--lns-color-backdropDark)}.md-c\:backdropTwilight{color:var(--lns-color-backdropTwilight)}.md-c\:disabledContent{color:var(--lns-color-disabledContent)}.md-c\:highlight{color:var(--lns-color-highlight)}.md-c\:disabledBackground{color:var(--lns-color-disabledBackground)}.md-c\:formFieldBorder{color:var(--lns-color-formFieldBorder)}.md-c\:formFieldBackground{color:var(--lns-color-formFieldBackground)}.md-c\:buttonBorder{color:var(--lns-color-buttonBorder)}.md-c\:upgrade{color:var(--lns-color-upgrade)}.md-c\:upgradeHover{color:var(--lns-color-upgradeHover)}.md-c\:upgradeActive{color:var(--lns-color-upgradeActive)}.md-c\:tabBackground{color:var(--lns-color-tabBackground)}.md-c\:discoveryBackground{color:var(--lns-color-discoveryBackground)}.md-c\:discoveryLightBackground{color:var(--lns-color-discoveryLightBackground)}.md-c\:discoveryTitle{color:var(--lns-color-discoveryTitle)}.md-c\:discoveryHighlight{color:var(--lns-color-discoveryHighlight)}.md-shadow\:small{box-shadow:var(--lns-shadow-small)}.md-shadow\:medium{box-shadow:var(--lns-shadow-medium)}.md-shadow\:large{box-shadow:var(--lns-shadow-large)}.md-radius\:medium{border-radius:var(--lns-radius-medium)}.md-radius\:large{border-radius:var(--lns-radius-large)}.md-radius\:xlarge{border-radius:var(--lns-radius-xlarge)}.md-radius\:full{border-radius:var(--lns-radius-full)}.md-bgc\:red{background-color:var(--lns-color-red)}.md-bgc\:blurpleLight{background-color:var(--lns-color-blurpleLight)}.md-bgc\:blurpleMedium{background-color:var(--lns-color-blurpleMedium)}.md-bgc\:blurple{background-color:var(--lns-color-blurple)}.md-bgc\:blurpleDark{background-color:var(--lns-color-blurpleDark)}.md-bgc\:offWhite{background-color:var(--lns-color-offWhite)}.md-bgc\:blueLight{background-color:var(--lns-color-blueLight)}.md-bgc\:blue{background-color:var(--lns-color-blue)}.md-bgc\:blueDark{background-color:var(--lns-color-blueDark)}.md-bgc\:orangeLight{background-color:var(--lns-color-orangeLight)}.md-bgc\:orange{background-color:var(--lns-color-orange)}.md-bgc\:orangeDark{background-color:var(--lns-color-orangeDark)}.md-bgc\:tealLight{background-color:var(--lns-color-tealLight)}.md-bgc\:teal{background-color:var(--lns-color-teal)}.md-bgc\:tealDark{background-color:var(--lns-color-tealDark)}.md-bgc\:yellowLight{background-color:var(--lns-color-yellowLight)}.md-bgc\:yellow{background-color:var(--lns-color-yellow)}.md-bgc\:yellowDark{background-color:var(--lns-color-yellowDark)}.md-bgc\:grey8{background-color:var(--lns-color-grey8)}.md-bgc\:grey7{background-color:var(--lns-color-grey7)}.md-bgc\:grey6{background-color:var(--lns-color-grey6)}.md-bgc\:grey5{background-color:var(--lns-color-grey5)}.md-bgc\:grey4{background-color:var(--lns-color-grey4)}.md-bgc\:grey3{background-color:var(--lns-color-grey3)}.md-bgc\:grey2{background-color:var(--lns-color-grey2)}.md-bgc\:grey1{background-color:var(--lns-color-grey1)}.md-bgc\:white{background-color:var(--lns-color-white)}.md-bgc\:primary{background-color:var(--lns-color-primary)}.md-bgc\:primaryHover{background-color:var(--lns-color-primaryHover)}.md-bgc\:primaryActive{background-color:var(--lns-color-primaryActive)}.md-bgc\:body{background-color:var(--lns-color-body)}.md-bgc\:bodyDimmed{background-color:var(--lns-color-bodyDimmed)}.md-bgc\:background{background-color:var(--lns-color-background)}.md-bgc\:backgroundHover{background-color:var(--lns-color-backgroundHover)}.md-bgc\:backgroundActive{background-color:var(--lns-color-backgroundActive)}.md-bgc\:backgroundSecondary{background-color:var(--lns-color-backgroundSecondary)}.md-bgc\:backgroundSecondary2{background-color:var(--lns-color-backgroundSecondary2)}.md-bgc\:overlay{background-color:var(--lns-color-overlay)}.md-bgc\:border{background-color:var(--lns-color-border)}.md-bgc\:focusRing{background-color:var(--lns-color-focusRing)}.md-bgc\:record{background-color:var(--lns-color-record)}.md-bgc\:recordHover{background-color:var(--lns-color-recordHover)}.md-bgc\:recordActive{background-color:var(--lns-color-recordActive)}.md-bgc\:info{background-color:var(--lns-color-info)}.md-bgc\:success{background-color:var(--lns-color-success)}.md-bgc\:warning{background-color:var(--lns-color-warning)}.md-bgc\:danger{background-color:var(--lns-color-danger)}.md-bgc\:dangerHover{background-color:var(--lns-color-dangerHover)}.md-bgc\:dangerActive{background-color:var(--lns-color-dangerActive)}.md-bgc\:backdrop{background-color:var(--lns-color-backdrop)}.md-bgc\:backdropDark{background-color:var(--lns-color-backdropDark)}.md-bgc\:backdropTwilight{background-color:var(--lns-color-backdropTwilight)}.md-bgc\:disabledContent{background-color:var(--lns-color-disabledContent)}.md-bgc\:highlight{background-color:var(--lns-color-highlight)}.md-bgc\:disabledBackground{background-color:var(--lns-color-disabledBackground)}.md-bgc\:formFieldBorder{background-color:var(--lns-color-formFieldBorder)}.md-bgc\:formFieldBackground{background-color:var(--lns-color-formFieldBackground)}.md-bgc\:buttonBorder{background-color:var(--lns-color-buttonBorder)}.md-bgc\:upgrade{background-color:var(--lns-color-upgrade)}.md-bgc\:upgradeHover{background-color:var(--lns-color-upgradeHover)}.md-bgc\:upgradeActive{background-color:var(--lns-color-upgradeActive)}.md-bgc\:tabBackground{background-color:var(--lns-color-tabBackground)}.md-bgc\:discoveryBackground{background-color:var(--lns-color-discoveryBackground)}.md-bgc\:discoveryLightBackground{background-color:var(--lns-color-discoveryLightBackground)}.md-bgc\:discoveryTitle{background-color:var(--lns-color-discoveryTitle)}.md-bgc\:discoveryHighlight{background-color:var(--lns-color-discoveryHighlight)}.md-m\:0{margin:0}.md-m\:auto{margin:auto}.md-m\:xsmall{margin:var(--lns-space-xsmall)}.md-m\:small{margin:var(--lns-space-small)}.md-m\:medium{margin:var(--lns-space-medium)}.md-m\:large{margin:var(--lns-space-large)}.md-m\:xlarge{margin:var(--lns-space-xlarge)}.md-m\:xxlarge{margin:var(--lns-space-xxlarge)}.md-mt\:0{margin-top:0}.md-mt\:auto{margin-top:auto}.md-mt\:xsmall{margin-top:var(--lns-space-xsmall)}.md-mt\:small{margin-top:var(--lns-space-small)}.md-mt\:medium{margin-top:var(--lns-space-medium)}.md-mt\:large{margin-top:var(--lns-space-large)}.md-mt\:xlarge{margin-top:var(--lns-space-xlarge)}.md-mt\:xxlarge{margin-top:var(--lns-space-xxlarge)}.md-mb\:0{margin-bottom:0}.md-mb\:auto{margin-bottom:auto}.md-mb\:xsmall{margin-bottom:var(--lns-space-xsmall)}.md-mb\:small{margin-bottom:var(--lns-space-small)}.md-mb\:medium{margin-bottom:var(--lns-space-medium)}.md-mb\:large{margin-bottom:var(--lns-space-large)}.md-mb\:xlarge{margin-bottom:var(--lns-space-xlarge)}.md-mb\:xxlarge{margin-bottom:var(--lns-space-xxlarge)}.md-ml\:0{margin-left:0}.md-ml\:auto{margin-left:auto}.md-ml\:xsmall{margin-left:var(--lns-space-xsmall)}.md-ml\:small{margin-left:var(--lns-space-small)}.md-ml\:medium{margin-left:var(--lns-space-medium)}.md-ml\:large{margin-left:var(--lns-space-large)}.md-ml\:xlarge{margin-left:var(--lns-space-xlarge)}.md-ml\:xxlarge{margin-left:var(--lns-space-xxlarge)}.md-mr\:0{margin-right:0}.md-mr\:auto{margin-right:auto}.md-mr\:xsmall{margin-right:var(--lns-space-xsmall)}.md-mr\:small{margin-right:var(--lns-space-small)}.md-mr\:medium{margin-right:var(--lns-space-medium)}.md-mr\:large{margin-right:var(--lns-space-large)}.md-mr\:xlarge{margin-right:var(--lns-space-xlarge)}.md-mr\:xxlarge{margin-right:var(--lns-space-xxlarge)}.md-mx\:0{margin-left:0;margin-right:0}.md-mx\:auto{margin-left:auto;margin-right:auto}.md-mx\:xsmall{margin-left:var(--lns-space-xsmall);margin-right:var(--lns-space-xsmall)}.md-mx\:small{margin-left:var(--lns-space-small);margin-right:var(--lns-space-small)}.md-mx\:medium{margin-left:var(--lns-space-medium);margin-right:var(--lns-space-medium)}.md-mx\:large{margin-left:var(--lns-space-large);margin-right:var(--lns-space-large)}.md-mx\:xlarge{margin-left:var(--lns-space-xlarge);margin-right:var(--lns-space-xlarge)}.md-mx\:xxlarge{margin-left:var(--lns-space-xxlarge);margin-right:var(--lns-space-xxlarge)}.md-my\:0{margin-top:0;margin-bottom:0}.md-my\:auto{margin-top:auto;margin-bottom:auto}.md-my\:xsmall{margin-top:var(--lns-space-xsmall);margin-bottom:var(--lns-space-xsmall)}.md-my\:small{margin-top:var(--lns-space-small);margin-bottom:var(--lns-space-small)}.md-my\:medium{margin-top:var(--lns-space-medium);margin-bottom:var(--lns-space-medium)}.md-my\:large{margin-top:var(--lns-space-large);margin-bottom:var(--lns-space-large)}.md-my\:xlarge{margin-top:var(--lns-space-xlarge);margin-bottom:var(--lns-space-xlarge)}.md-my\:xxlarge{margin-top:var(--lns-space-xxlarge);margin-bottom:var(--lns-space-xxlarge)}.md-p\:0{padding:0}.md-p\:xsmall{padding:var(--lns-space-xsmall)}.md-p\:small{padding:var(--lns-space-small)}.md-p\:medium{padding:var(--lns-space-medium)}.md-p\:large{padding:var(--lns-space-large)}.md-p\:xlarge{padding:var(--lns-space-xlarge)}.md-p\:xxlarge{padding:var(--lns-space-xxlarge)}.md-pt\:0{padding-top:0}.md-pt\:xsmall{padding-top:var(--lns-space-xsmall)}.md-pt\:small{padding-top:var(--lns-space-small)}.md-pt\:medium{padding-top:var(--lns-space-medium)}.md-pt\:large{padding-top:var(--lns-space-large)}.md-pt\:xlarge{padding-top:var(--lns-space-xlarge)}.md-pt\:xxlarge{padding-top:var(--lns-space-xxlarge)}.md-pb\:0{padding-bottom:0}.md-pb\:xsmall{padding-bottom:var(--lns-space-xsmall)}.md-pb\:small{padding-bottom:var(--lns-space-small)}.md-pb\:medium{padding-bottom:var(--lns-space-medium)}.md-pb\:large{padding-bottom:var(--lns-space-large)}.md-pb\:xlarge{padding-bottom:var(--lns-space-xlarge)}.md-pb\:xxlarge{padding-bottom:var(--lns-space-xxlarge)}.md-pl\:0{padding-left:0}.md-pl\:xsmall{padding-left:var(--lns-space-xsmall)}.md-pl\:small{padding-left:var(--lns-space-small)}.md-pl\:medium{padding-left:var(--lns-space-medium)}.md-pl\:large{padding-left:var(--lns-space-large)}.md-pl\:xlarge{padding-left:var(--lns-space-xlarge)}.md-pl\:xxlarge{padding-left:var(--lns-space-xxlarge)}.md-pr\:0{padding-right:0}.md-pr\:xsmall{padding-right:var(--lns-space-xsmall)}.md-pr\:small{padding-right:var(--lns-space-small)}.md-pr\:medium{padding-right:var(--lns-space-medium)}.md-pr\:large{padding-right:var(--lns-space-large)}.md-pr\:xlarge{padding-right:var(--lns-space-xlarge)}.md-pr\:xxlarge{padding-right:var(--lns-space-xxlarge)}.md-px\:0{padding-left:0;padding-right:0}.md-px\:xsmall{padding-left:var(--lns-space-xsmall);padding-right:var(--lns-space-xsmall)}.md-px\:small{padding-left:var(--lns-space-small);padding-right:var(--lns-space-small)}.md-px\:medium{padding-left:var(--lns-space-medium);padding-right:var(--lns-space-medium)}.md-px\:large{padding-left:var(--lns-space-large);padding-right:var(--lns-space-large)}.md-px\:xlarge{padding-left:var(--lns-space-xlarge);padding-right:var(--lns-space-xlarge)}.md-px\:xxlarge{padding-left:var(--lns-space-xxlarge);padding-right:var(--lns-space-xxlarge)}.md-py\:0{padding-top:0;padding-bottom:0}.md-py\:xsmall{padding-top:var(--lns-space-xsmall);padding-bottom:var(--lns-space-xsmall)}.md-py\:small{padding-top:var(--lns-space-small);padding-bottom:var(--lns-space-small)}.md-py\:medium{padding-top:var(--lns-space-medium);padding-bottom:var(--lns-space-medium)}.md-py\:large{padding-top:var(--lns-space-large);padding-bottom:var(--lns-space-large)}.md-py\:xlarge{padding-top:var(--lns-space-xlarge);padding-bottom:var(--lns-space-xlarge)}.md-py\:xxlarge{padding-top:var(--lns-space-xxlarge);padding-bottom:var(--lns-space-xxlarge)}.md-text\:small{font-size:var(--lns-fontSize-small);line-height:var(--lns-lineHeight-small)}.md-text\:body-sm{font-size:var(--lns-fontSize-body-sm);line-height:var(--lns-lineHeight-body-sm)}.md-text\:medium{font-size:var(--lns-fontSize-medium);line-height:var(--lns-lineHeight-medium)}.md-text\:body-md{font-size:var(--lns-fontSize-body-md);line-height:var(--lns-lineHeight-body-md)}.md-text\:large{font-size:var(--lns-fontSize-large);line-height:var(--lns-lineHeight-large)}.md-text\:body-lg{font-size:var(--lns-fontSize-body-lg);line-height:var(--lns-lineHeight-body-lg)}.md-text\:xlarge{font-size:var(--lns-fontSize-xlarge);line-height:var(--lns-lineHeight-xlarge)}.md-text\:heading-sm{font-size:var(--lns-fontSize-heading-sm);line-height:var(--lns-lineHeight-heading-sm)}.md-text\:xxlarge{font-size:var(--lns-fontSize-xxlarge);line-height:var(--lns-lineHeight-xxlarge)}.md-text\:heading-md{font-size:var(--lns-fontSize-heading-md);line-height:var(--lns-lineHeight-heading-md)}.md-text\:xxxlarge{font-size:var(--lns-fontSize-xxxlarge);line-height:var(--lns-lineHeight-xxxlarge)}.md-text\:heading-lg{font-size:var(--lns-fontSize-heading-lg);line-height:var(--lns-lineHeight-heading-lg)}.md-weight\:book{font-weight:var(--lns-fontWeight-book)}.md-weight\:bold{font-weight:var(--lns-fontWeight-bold)}.md-text\:body{font-size:var(--lns-fontSize-body-md);line-height:var(--lns-lineHeight-body-md);font-weight:var(--lns-fontWeight-book)}.md-text\:title{font-size:var(--lns-fontSize-body-lg);line-height:var(--lns-lineHeight-body-lg);font-weight:var(--lns-fontWeight-bold)}.md-text\:mainTitle{font-size:var(--lns-fontSize-heading-md);line-height:var(--lns-lineHeight-heading-md);font-weight:var(--lns-fontWeight-bold)}.md-text\:left{text-align:left}.md-text\:right{text-align:right}.md-text\:center{text-align:center}.md-border{border:1px solid var(--lns-color-border)}.md-borderTop{border-top:1px solid var(--lns-color-border)}.md-borderBottom{border-bottom:1px solid var(--lns-color-border)}.md-borderLeft{border-left:1px solid var(--lns-color-border)}.md-borderRight{border-right:1px solid var(--lns-color-border)}.md-inline{display:inline}.md-block{display:block}.md-flex{display:flex}.md-inlineBlock{display:inline-block}.md-inlineFlex{display:inline-flex}.md-none{display:none}.md-flexWrap{flex-wrap:wrap}.md-flexDirection\:column{flex-direction:column}.md-flexDirection\:row{flex-direction:row}.md-items\:stretch{align-items:stretch}.md-items\:center{align-items:center}.md-items\:baseline{align-items:baseline}.md-items\:flexStart{align-items:flex-start}.md-items\:flexEnd{align-items:flex-end}.md-items\:selfStart{align-items:self-start}.md-items\:selfEnd{align-items:self-end}.md-justify\:flexStart{justify-content:flex-start}.md-justify\:flexEnd{justify-content:flex-end}.md-justify\:center{justify-content:center}.md-justify\:spaceBetween{justify-content:space-between}.md-justify\:spaceAround{justify-content:space-around}.md-justify\:spaceEvenly{justify-content:space-evenly}.md-grow\:0{flex-grow:0}.md-grow\:1{flex-grow:1}.md-shrink\:0{flex-shrink:0}.md-shrink\:1{flex-shrink:1}.md-self\:auto{align-self:auto}.md-self\:flexStart{align-self:flex-start}.md-self\:flexEnd{align-self:flex-end}.md-self\:center{align-self:center}.md-self\:baseline{align-self:baseline}.md-self\:stretch{align-self:stretch}.md-overflow\:hidden{overflow:hidden}.md-overflow\:auto{overflow:auto}.md-relative{position:relative}.md-absolute{position:absolute}.md-sticky{position:sticky}.md-fixed{position:fixed}.md-top\:0{top:0}.md-top\:auto{top:auto}.md-top\:xsmall{top:var(--lns-space-xsmall)}.md-top\:small{top:var(--lns-space-small)}.md-top\:medium{top:var(--lns-space-medium)}.md-top\:large{top:var(--lns-space-large)}.md-top\:xlarge{top:var(--lns-space-xlarge)}.md-top\:xxlarge{top:var(--lns-space-xxlarge)}.md-bottom\:0{bottom:0}.md-bottom\:auto{bottom:auto}.md-bottom\:xsmall{bottom:var(--lns-space-xsmall)}.md-bottom\:small{bottom:var(--lns-space-small)}.md-bottom\:medium{bottom:var(--lns-space-medium)}.md-bottom\:large{bottom:var(--lns-space-large)}.md-bottom\:xlarge{bottom:var(--lns-space-xlarge)}.md-bottom\:xxlarge{bottom:var(--lns-space-xxlarge)}.md-left\:0{left:0}.md-left\:auto{left:auto}.md-left\:xsmall{left:var(--lns-space-xsmall)}.md-left\:small{left:var(--lns-space-small)}.md-left\:medium{left:var(--lns-space-medium)}.md-left\:large{left:var(--lns-space-large)}.md-left\:xlarge{left:var(--lns-space-xlarge)}.md-left\:xxlarge{left:var(--lns-space-xxlarge)}.md-right\:0{right:0}.md-right\:auto{right:auto}.md-right\:xsmall{right:var(--lns-space-xsmall)}.md-right\:small{right:var(--lns-space-small)}.md-right\:medium{right:var(--lns-space-medium)}.md-right\:large{right:var(--lns-space-large)}.md-right\:xlarge{right:var(--lns-space-xlarge)}.md-right\:xxlarge{right:var(--lns-space-xxlarge)}.md-width\:auto{width:auto}.md-width\:full{width:100%}.md-width\:0{width:0}.md-minWidth\:0{min-width:0}.md-height\:auto{height:auto}.md-height\:full{height:100%}.md-height\:0{height:0}.md-ellipsis{overflow:hidden;text-overflow:ellipsis;white-space:nowrap}.md-srOnly{position:absolute;width:1px;height:1px;padding:0;margin:-1px;overflow:hidden;clip:rect(0, 0, 0, 0);white-space:nowrap;border-width:0}}@media(min-width:75em){.lg-c\:red{color:var(--lns-color-red)}.lg-c\:blurpleLight{color:var(--lns-color-blurpleLight)}.lg-c\:blurpleMedium{color:var(--lns-color-blurpleMedium)}.lg-c\:blurple{color:var(--lns-color-blurple)}.lg-c\:blurpleDark{color:var(--lns-color-blurpleDark)}.lg-c\:offWhite{color:var(--lns-color-offWhite)}.lg-c\:blueLight{color:var(--lns-color-blueLight)}.lg-c\:blue{color:var(--lns-color-blue)}.lg-c\:blueDark{color:var(--lns-color-blueDark)}.lg-c\:orangeLight{color:var(--lns-color-orangeLight)}.lg-c\:orange{color:var(--lns-color-orange)}.lg-c\:orangeDark{color:var(--lns-color-orangeDark)}.lg-c\:tealLight{color:var(--lns-color-tealLight)}.lg-c\:teal{color:var(--lns-color-teal)}.lg-c\:tealDark{color:var(--lns-color-tealDark)}.lg-c\:yellowLight{color:var(--lns-color-yellowLight)}.lg-c\:yellow{color:var(--lns-color-yellow)}.lg-c\:yellowDark{color:var(--lns-color-yellowDark)}.lg-c\:grey8{color:var(--lns-color-grey8)}.lg-c\:grey7{color:var(--lns-color-grey7)}.lg-c\:grey6{color:var(--lns-color-grey6)}.lg-c\:grey5{color:var(--lns-color-grey5)}.lg-c\:grey4{color:var(--lns-color-grey4)}.lg-c\:grey3{color:var(--lns-color-grey3)}.lg-c\:grey2{color:var(--lns-color-grey2)}.lg-c\:grey1{color:var(--lns-color-grey1)}.lg-c\:white{color:var(--lns-color-white)}.lg-c\:primary{color:var(--lns-color-primary)}.lg-c\:primaryHover{color:var(--lns-color-primaryHover)}.lg-c\:primaryActive{color:var(--lns-color-primaryActive)}.lg-c\:body{color:var(--lns-color-body)}.lg-c\:bodyDimmed{color:var(--lns-color-bodyDimmed)}.lg-c\:background{color:var(--lns-color-background)}.lg-c\:backgroundHover{color:var(--lns-color-backgroundHover)}.lg-c\:backgroundActive{color:var(--lns-color-backgroundActive)}.lg-c\:backgroundSecondary{color:var(--lns-color-backgroundSecondary)}.lg-c\:backgroundSecondary2{color:var(--lns-color-backgroundSecondary2)}.lg-c\:overlay{color:var(--lns-color-overlay)}.lg-c\:border{color:var(--lns-color-border)}.lg-c\:focusRing{color:var(--lns-color-focusRing)}.lg-c\:record{color:var(--lns-color-record)}.lg-c\:recordHover{color:var(--lns-color-recordHover)}.lg-c\:recordActive{color:var(--lns-color-recordActive)}.lg-c\:info{color:var(--lns-color-info)}.lg-c\:success{color:var(--lns-color-success)}.lg-c\:warning{color:var(--lns-color-warning)}.lg-c\:danger{color:var(--lns-color-danger)}.lg-c\:dangerHover{color:var(--lns-color-dangerHover)}.lg-c\:dangerActive{color:var(--lns-color-dangerActive)}.lg-c\:backdrop{color:var(--lns-color-backdrop)}.lg-c\:backdropDark{color:var(--lns-color-backdropDark)}.lg-c\:backdropTwilight{color:var(--lns-color-backdropTwilight)}.lg-c\:disabledContent{color:var(--lns-color-disabledContent)}.lg-c\:highlight{color:var(--lns-color-highlight)}.lg-c\:disabledBackground{color:var(--lns-color-disabledBackground)}.lg-c\:formFieldBorder{color:var(--lns-color-formFieldBorder)}.lg-c\:formFieldBackground{color:var(--lns-color-formFieldBackground)}.lg-c\:buttonBorder{color:var(--lns-color-buttonBorder)}.lg-c\:upgrade{color:var(--lns-color-upgrade)}.lg-c\:upgradeHover{color:var(--lns-color-upgradeHover)}.lg-c\:upgradeActive{color:var(--lns-color-upgradeActive)}.lg-c\:tabBackground{color:var(--lns-color-tabBackground)}.lg-c\:discoveryBackground{color:var(--lns-color-discoveryBackground)}.lg-c\:discoveryLightBackground{color:var(--lns-color-discoveryLightBackground)}.lg-c\:discoveryTitle{color:var(--lns-color-discoveryTitle)}.lg-c\:discoveryHighlight{color:var(--lns-color-discoveryHighlight)}.lg-shadow\:small{box-shadow:var(--lns-shadow-small)}.lg-shadow\:medium{box-shadow:var(--lns-shadow-medium)}.lg-shadow\:large{box-shadow:var(--lns-shadow-large)}.lg-radius\:medium{border-radius:var(--lns-radius-medium)}.lg-radius\:large{border-radius:var(--lns-radius-large)}.lg-radius\:xlarge{border-radius:var(--lns-radius-xlarge)}.lg-radius\:full{border-radius:var(--lns-radius-full)}.lg-bgc\:red{background-color:var(--lns-color-red)}.lg-bgc\:blurpleLight{background-color:var(--lns-color-blurpleLight)}.lg-bgc\:blurpleMedium{background-color:var(--lns-color-blurpleMedium)}.lg-bgc\:blurple{background-color:var(--lns-color-blurple)}.lg-bgc\:blurpleDark{background-color:var(--lns-color-blurpleDark)}.lg-bgc\:offWhite{background-color:var(--lns-color-offWhite)}.lg-bgc\:blueLight{background-color:var(--lns-color-blueLight)}.lg-bgc\:blue{background-color:var(--lns-color-blue)}.lg-bgc\:blueDark{background-color:var(--lns-color-blueDark)}.lg-bgc\:orangeLight{background-color:var(--lns-color-orangeLight)}.lg-bgc\:orange{background-color:var(--lns-color-orange)}.lg-bgc\:orangeDark{background-color:var(--lns-color-orangeDark)}.lg-bgc\:tealLight{background-color:var(--lns-color-tealLight)}.lg-bgc\:teal{background-color:var(--lns-color-teal)}.lg-bgc\:tealDark{background-color:var(--lns-color-tealDark)}.lg-bgc\:yellowLight{background-color:var(--lns-color-yellowLight)}.lg-bgc\:yellow{background-color:var(--lns-color-yellow)}.lg-bgc\:yellowDark{background-color:var(--lns-color-yellowDark)}.lg-bgc\:grey8{background-color:var(--lns-color-grey8)}.lg-bgc\:grey7{background-color:var(--lns-color-grey7)}.lg-bgc\:grey6{background-color:var(--lns-color-grey6)}.lg-bgc\:grey5{background-color:var(--lns-color-grey5)}.lg-bgc\:grey4{background-color:var(--lns-color-grey4)}.lg-bgc\:grey3{background-color:var(--lns-color-grey3)}.lg-bgc\:grey2{background-color:var(--lns-color-grey2)}.lg-bgc\:grey1{background-color:var(--lns-color-grey1)}.lg-bgc\:white{background-color:var(--lns-color-white)}.lg-bgc\:primary{background-color:var(--lns-color-primary)}.lg-bgc\:primaryHover{background-color:var(--lns-color-primaryHover)}.lg-bgc\:primaryActive{background-color:var(--lns-color-primaryActive)}.lg-bgc\:body{background-color:var(--lns-color-body)}.lg-bgc\:bodyDimmed{background-color:var(--lns-color-bodyDimmed)}.lg-bgc\:background{background-color:var(--lns-color-background)}.lg-bgc\:backgroundHover{background-color:var(--lns-color-backgroundHover)}.lg-bgc\:backgroundActive{background-color:var(--lns-color-backgroundActive)}.lg-bgc\:backgroundSecondary{background-color:var(--lns-color-backgroundSecondary)}.lg-bgc\:backgroundSecondary2{background-color:var(--lns-color-backgroundSecondary2)}.lg-bgc\:overlay{background-color:var(--lns-color-overlay)}.lg-bgc\:border{background-color:var(--lns-color-border)}.lg-bgc\:focusRing{background-color:var(--lns-color-focusRing)}.lg-bgc\:record{background-color:var(--lns-color-record)}.lg-bgc\:recordHover{background-color:var(--lns-color-recordHover)}.lg-bgc\:recordActive{background-color:var(--lns-color-recordActive)}.lg-bgc\:info{background-color:var(--lns-color-info)}.lg-bgc\:success{background-color:var(--lns-color-success)}.lg-bgc\:warning{background-color:var(--lns-color-warning)}.lg-bgc\:danger{background-color:var(--lns-color-danger)}.lg-bgc\:dangerHover{background-color:var(--lns-color-dangerHover)}.lg-bgc\:dangerActive{background-color:var(--lns-color-dangerActive)}.lg-bgc\:backdrop{background-color:var(--lns-color-backdrop)}.lg-bgc\:backdropDark{background-color:var(--lns-color-backdropDark)}.lg-bgc\:backdropTwilight{background-color:var(--lns-color-backdropTwilight)}.lg-bgc\:disabledContent{background-color:var(--lns-color-disabledContent)}.lg-bgc\:highlight{background-color:var(--lns-color-highlight)}.lg-bgc\:disabledBackground{background-color:var(--lns-color-disabledBackground)}.lg-bgc\:formFieldBorder{background-color:var(--lns-color-formFieldBorder)}.lg-bgc\:formFieldBackground{background-color:var(--lns-color-formFieldBackground)}.lg-bgc\:buttonBorder{background-color:var(--lns-color-buttonBorder)}.lg-bgc\:upgrade{background-color:var(--lns-color-upgrade)}.lg-bgc\:upgradeHover{background-color:var(--lns-color-upgradeHover)}.lg-bgc\:upgradeActive{background-color:var(--lns-color-upgradeActive)}.lg-bgc\:tabBackground{background-color:var(--lns-color-tabBackground)}.lg-bgc\:discoveryBackground{background-color:var(--lns-color-discoveryBackground)}.lg-bgc\:discoveryLightBackground{background-color:var(--lns-color-discoveryLightBackground)}.lg-bgc\:discoveryTitle{background-color:var(--lns-color-discoveryTitle)}.lg-bgc\:discoveryHighlight{background-color:var(--lns-color-discoveryHighlight)}.lg-m\:0{margin:0}.lg-m\:auto{margin:auto}.lg-m\:xsmall{margin:var(--lns-space-xsmall)}.lg-m\:small{margin:var(--lns-space-small)}.lg-m\:medium{margin:var(--lns-space-medium)}.lg-m\:large{margin:var(--lns-space-large)}.lg-m\:xlarge{margin:var(--lns-space-xlarge)}.lg-m\:xxlarge{margin:var(--lns-space-xxlarge)}.lg-mt\:0{margin-top:0}.lg-mt\:auto{margin-top:auto}.lg-mt\:xsmall{margin-top:var(--lns-space-xsmall)}.lg-mt\:small{margin-top:var(--lns-space-small)}.lg-mt\:medium{margin-top:var(--lns-space-medium)}.lg-mt\:large{margin-top:var(--lns-space-large)}.lg-mt\:xlarge{margin-top:var(--lns-space-xlarge)}.lg-mt\:xxlarge{margin-top:var(--lns-space-xxlarge)}.lg-mb\:0{margin-bottom:0}.lg-mb\:auto{margin-bottom:auto}.lg-mb\:xsmall{margin-bottom:var(--lns-space-xsmall)}.lg-mb\:small{margin-bottom:var(--lns-space-small)}.lg-mb\:medium{margin-bottom:var(--lns-space-medium)}.lg-mb\:large{margin-bottom:var(--lns-space-large)}.lg-mb\:xlarge{margin-bottom:var(--lns-space-xlarge)}.lg-mb\:xxlarge{margin-bottom:var(--lns-space-xxlarge)}.lg-ml\:0{margin-left:0}.lg-ml\:auto{margin-left:auto}.lg-ml\:xsmall{margin-left:var(--lns-space-xsmall)}.lg-ml\:small{margin-left:var(--lns-space-small)}.lg-ml\:medium{margin-left:var(--lns-space-medium)}.lg-ml\:large{margin-left:var(--lns-space-large)}.lg-ml\:xlarge{margin-left:var(--lns-space-xlarge)}.lg-ml\:xxlarge{margin-left:var(--lns-space-xxlarge)}.lg-mr\:0{margin-right:0}.lg-mr\:auto{margin-right:auto}.lg-mr\:xsmall{margin-right:var(--lns-space-xsmall)}.lg-mr\:small{margin-right:var(--lns-space-small)}.lg-mr\:medium{margin-right:var(--lns-space-medium)}.lg-mr\:large{margin-right:var(--lns-space-large)}.lg-mr\:xlarge{margin-right:var(--lns-space-xlarge)}.lg-mr\:xxlarge{margin-right:var(--lns-space-xxlarge)}.lg-mx\:0{margin-left:0;margin-right:0}.lg-mx\:auto{margin-left:auto;margin-right:auto}.lg-mx\:xsmall{margin-left:var(--lns-space-xsmall);margin-right:var(--lns-space-xsmall)}.lg-mx\:small{margin-left:var(--lns-space-small);margin-right:var(--lns-space-small)}.lg-mx\:medium{margin-left:var(--lns-space-medium);margin-right:var(--lns-space-medium)}.lg-mx\:large{margin-left:var(--lns-space-large);margin-right:var(--lns-space-large)}.lg-mx\:xlarge{margin-left:var(--lns-space-xlarge);margin-right:var(--lns-space-xlarge)}.lg-mx\:xxlarge{margin-left:var(--lns-space-xxlarge);margin-right:var(--lns-space-xxlarge)}.lg-my\:0{margin-top:0;margin-bottom:0}.lg-my\:auto{margin-top:auto;margin-bottom:auto}.lg-my\:xsmall{margin-top:var(--lns-space-xsmall);margin-bottom:var(--lns-space-xsmall)}.lg-my\:small{margin-top:var(--lns-space-small);margin-bottom:var(--lns-space-small)}.lg-my\:medium{margin-top:var(--lns-space-medium);margin-bottom:var(--lns-space-medium)}.lg-my\:large{margin-top:var(--lns-space-large);margin-bottom:var(--lns-space-large)}.lg-my\:xlarge{margin-top:var(--lns-space-xlarge);margin-bottom:var(--lns-space-xlarge)}.lg-my\:xxlarge{margin-top:var(--lns-space-xxlarge);margin-bottom:var(--lns-space-xxlarge)}.lg-p\:0{padding:0}.lg-p\:xsmall{padding:var(--lns-space-xsmall)}.lg-p\:small{padding:var(--lns-space-small)}.lg-p\:medium{padding:var(--lns-space-medium)}.lg-p\:large{padding:var(--lns-space-large)}.lg-p\:xlarge{padding:var(--lns-space-xlarge)}.lg-p\:xxlarge{padding:var(--lns-space-xxlarge)}.lg-pt\:0{padding-top:0}.lg-pt\:xsmall{padding-top:var(--lns-space-xsmall)}.lg-pt\:small{padding-top:var(--lns-space-small)}.lg-pt\:medium{padding-top:var(--lns-space-medium)}.lg-pt\:large{padding-top:var(--lns-space-large)}.lg-pt\:xlarge{padding-top:var(--lns-space-xlarge)}.lg-pt\:xxlarge{padding-top:var(--lns-space-xxlarge)}.lg-pb\:0{padding-bottom:0}.lg-pb\:xsmall{padding-bottom:var(--lns-space-xsmall)}.lg-pb\:small{padding-bottom:var(--lns-space-small)}.lg-pb\:medium{padding-bottom:var(--lns-space-medium)}.lg-pb\:large{padding-bottom:var(--lns-space-large)}.lg-pb\:xlarge{padding-bottom:var(--lns-space-xlarge)}.lg-pb\:xxlarge{padding-bottom:var(--lns-space-xxlarge)}.lg-pl\:0{padding-left:0}.lg-pl\:xsmall{padding-left:var(--lns-space-xsmall)}.lg-pl\:small{padding-left:var(--lns-space-small)}.lg-pl\:medium{padding-left:var(--lns-space-medium)}.lg-pl\:large{padding-left:var(--lns-space-large)}.lg-pl\:xlarge{padding-left:var(--lns-space-xlarge)}.lg-pl\:xxlarge{padding-left:var(--lns-space-xxlarge)}.lg-pr\:0{padding-right:0}.lg-pr\:xsmall{padding-right:var(--lns-space-xsmall)}.lg-pr\:small{padding-right:var(--lns-space-small)}.lg-pr\:medium{padding-right:var(--lns-space-medium)}.lg-pr\:large{padding-right:var(--lns-space-large)}.lg-pr\:xlarge{padding-right:var(--lns-space-xlarge)}.lg-pr\:xxlarge{padding-right:var(--lns-space-xxlarge)}.lg-px\:0{padding-left:0;padding-right:0}.lg-px\:xsmall{padding-left:var(--lns-space-xsmall);padding-right:var(--lns-space-xsmall)}.lg-px\:small{padding-left:var(--lns-space-small);padding-right:var(--lns-space-small)}.lg-px\:medium{padding-left:var(--lns-space-medium);padding-right:var(--lns-space-medium)}.lg-px\:large{padding-left:var(--lns-space-large);padding-right:var(--lns-space-large)}.lg-px\:xlarge{padding-left:var(--lns-space-xlarge);padding-right:var(--lns-space-xlarge)}.lg-px\:xxlarge{padding-left:var(--lns-space-xxlarge);padding-right:var(--lns-space-xxlarge)}.lg-py\:0{padding-top:0;padding-bottom:0}.lg-py\:xsmall{padding-top:var(--lns-space-xsmall);padding-bottom:var(--lns-space-xsmall)}.lg-py\:small{padding-top:var(--lns-space-small);padding-bottom:var(--lns-space-small)}.lg-py\:medium{padding-top:var(--lns-space-medium);padding-bottom:var(--lns-space-medium)}.lg-py\:large{padding-top:var(--lns-space-large);padding-bottom:var(--lns-space-large)}.lg-py\:xlarge{padding-top:var(--lns-space-xlarge);padding-bottom:var(--lns-space-xlarge)}.lg-py\:xxlarge{padding-top:var(--lns-space-xxlarge);padding-bottom:var(--lns-space-xxlarge)}.lg-text\:small{font-size:var(--lns-fontSize-small);line-height:var(--lns-lineHeight-small)}.lg-text\:body-sm{font-size:var(--lns-fontSize-body-sm);line-height:var(--lns-lineHeight-body-sm)}.lg-text\:medium{font-size:var(--lns-fontSize-medium);line-height:var(--lns-lineHeight-medium)}.lg-text\:body-md{font-size:var(--lns-fontSize-body-md);line-height:var(--lns-lineHeight-body-md)}.lg-text\:large{font-size:var(--lns-fontSize-large);line-height:var(--lns-lineHeight-large)}.lg-text\:body-lg{font-size:var(--lns-fontSize-body-lg);line-height:var(--lns-lineHeight-body-lg)}.lg-text\:xlarge{font-size:var(--lns-fontSize-xlarge);line-height:var(--lns-lineHeight-xlarge)}.lg-text\:heading-sm{font-size:var(--lns-fontSize-heading-sm);line-height:var(--lns-lineHeight-heading-sm)}.lg-text\:xxlarge{font-size:var(--lns-fontSize-xxlarge);line-height:var(--lns-lineHeight-xxlarge)}.lg-text\:heading-md{font-size:var(--lns-fontSize-heading-md);line-height:var(--lns-lineHeight-heading-md)}.lg-text\:xxxlarge{font-size:var(--lns-fontSize-xxxlarge);line-height:var(--lns-lineHeight-xxxlarge)}.lg-text\:heading-lg{font-size:var(--lns-fontSize-heading-lg);line-height:var(--lns-lineHeight-heading-lg)}.lg-weight\:book{font-weight:var(--lns-fontWeight-book)}.lg-weight\:bold{font-weight:var(--lns-fontWeight-bold)}.lg-text\:body{font-size:var(--lns-fontSize-body-md);line-height:var(--lns-lineHeight-body-md);font-weight:var(--lns-fontWeight-book)}.lg-text\:title{font-size:var(--lns-fontSize-body-lg);line-height:var(--lns-lineHeight-body-lg);font-weight:var(--lns-fontWeight-bold)}.lg-text\:mainTitle{font-size:var(--lns-fontSize-heading-md);line-height:var(--lns-lineHeight-heading-md);font-weight:var(--lns-fontWeight-bold)}.lg-text\:left{text-align:left}.lg-text\:right{text-align:right}.lg-text\:center{text-align:center}.lg-border{border:1px solid var(--lns-color-border)}.lg-borderTop{border-top:1px solid var(--lns-color-border)}.lg-borderBottom{border-bottom:1px solid var(--lns-color-border)}.lg-borderLeft{border-left:1px solid var(--lns-color-border)}.lg-borderRight{border-right:1px solid var(--lns-color-border)}.lg-inline{display:inline}.lg-block{display:block}.lg-flex{display:flex}.lg-inlineBlock{display:inline-block}.lg-inlineFlex{display:inline-flex}.lg-none{display:none}.lg-flexWrap{flex-wrap:wrap}.lg-flexDirection\:column{flex-direction:column}.lg-flexDirection\:row{flex-direction:row}.lg-items\:stretch{align-items:stretch}.lg-items\:center{align-items:center}.lg-items\:baseline{align-items:baseline}.lg-items\:flexStart{align-items:flex-start}.lg-items\:flexEnd{align-items:flex-end}.lg-items\:selfStart{align-items:self-start}.lg-items\:selfEnd{align-items:self-end}.lg-justify\:flexStart{justify-content:flex-start}.lg-justify\:flexEnd{justify-content:flex-end}.lg-justify\:center{justify-content:center}.lg-justify\:spaceBetween{justify-content:space-between}.lg-justify\:spaceAround{justify-content:space-around}.lg-justify\:spaceEvenly{justify-content:space-evenly}.lg-grow\:0{flex-grow:0}.lg-grow\:1{flex-grow:1}.lg-shrink\:0{flex-shrink:0}.lg-shrink\:1{flex-shrink:1}.lg-self\:auto{align-self:auto}.lg-self\:flexStart{align-self:flex-start}.lg-self\:flexEnd{align-self:flex-end}.lg-self\:center{align-self:center}.lg-self\:baseline{align-self:baseline}.lg-self\:stretch{align-self:stretch}.lg-overflow\:hidden{overflow:hidden}.lg-overflow\:auto{overflow:auto}.lg-relative{position:relative}.lg-absolute{position:absolute}.lg-sticky{position:sticky}.lg-fixed{position:fixed}.lg-top\:0{top:0}.lg-top\:auto{top:auto}.lg-top\:xsmall{top:var(--lns-space-xsmall)}.lg-top\:small{top:var(--lns-space-small)}.lg-top\:medium{top:var(--lns-space-medium)}.lg-top\:large{top:var(--lns-space-large)}.lg-top\:xlarge{top:var(--lns-space-xlarge)}.lg-top\:xxlarge{top:var(--lns-space-xxlarge)}.lg-bottom\:0{bottom:0}.lg-bottom\:auto{bottom:auto}.lg-bottom\:xsmall{bottom:var(--lns-space-xsmall)}.lg-bottom\:small{bottom:var(--lns-space-small)}.lg-bottom\:medium{bottom:var(--lns-space-medium)}.lg-bottom\:large{bottom:var(--lns-space-large)}.lg-bottom\:xlarge{bottom:var(--lns-space-xlarge)}.lg-bottom\:xxlarge{bottom:var(--lns-space-xxlarge)}.lg-left\:0{left:0}.lg-left\:auto{left:auto}.lg-left\:xsmall{left:var(--lns-space-xsmall)}.lg-left\:small{left:var(--lns-space-small)}.lg-left\:medium{left:var(--lns-space-medium)}.lg-left\:large{left:var(--lns-space-large)}.lg-left\:xlarge{left:var(--lns-space-xlarge)}.lg-left\:xxlarge{left:var(--lns-space-xxlarge)}.lg-right\:0{right:0}.lg-right\:auto{right:auto}.lg-right\:xsmall{right:var(--lns-space-xsmall)}.lg-right\:small{right:var(--lns-space-small)}.lg-right\:medium{right:var(--lns-space-medium)}.lg-right\:large{right:var(--lns-space-large)}.lg-right\:xlarge{right:var(--lns-space-xlarge)}.lg-right\:xxlarge{right:var(--lns-space-xxlarge)}.lg-width\:auto{width:auto}.lg-width\:full{width:100%}.lg-width\:0{width:0}.lg-minWidth\:0{min-width:0}.lg-height\:auto{height:auto}.lg-height\:full{height:100%}.lg-height\:0{height:0}.lg-ellipsis{overflow:hidden;text-overflow:ellipsis;white-space:nowrap}.lg-srOnly{position:absolute;width:1px;height:1px;padding:0;margin:-1px;overflow:hidden;clip:rect(0, 0, 0, 0);white-space:nowrap;border-width:0}}
  
            #inner-shadow-companion {
              --lns-unit: 8px;
              all: initial;
              font-family: circular, Helvetica, sans-serif;
              color: var(--lns-color-body);
            }
            #tooltip-mount-layer-companion {
              z-index: 2147483646;
              position: relative;

              color: var(--lns-color-body);
              pointer-events: auto;
            }
          </style><div class="companion-1b6rwsq"></div></div></template></section></div><div style="position: absolute; width: 0px; height: 0px; overflow: hidden; padding: 0px; border: 0px; margin: 0px;"><div id="MathJax_Font_Test" style="position: absolute; visibility: hidden; top: 0px; left: 0px; width: auto; min-width: 0px; max-width: none; padding: 0px; border: 0px; margin: 0px; white-space: nowrap; text-align: left; text-indent: 0px; text-transform: none; line-height: normal; letter-spacing: normal; word-spacing: normal; font-size: 40px; font-weight: normal; font-style: normal; font-family: MathJax_Size1, monospace;"></div></div><div class="notebook-vertical" style="position: relative;">
      <div class="top-floater"><div role="banner">
    <colab-header-skip-button><template shadowrootmode="open"><!----><a id="skiplink" class="skip-link" href="https://colab.research.google.com/drive/1UQ9tc9AaVNd7WtJUnMArlHDBSayfozb8#top-toolbar"><!--?lit$571398431$-->Skip to main content</a></template></colab-header-skip-button>
    <!--?lit$571398431$-->
    <!--?lit$571398431$-->
    <!--?lit$571398431$-->
          <div id="private-outputs-warning" class="header-warning private-outputs-warning hidden">
            <!--?lit$571398431$-->This notebook is open with private outputs. Outputs will not be saved. You can disable this in <a href="https://colab.research.google.com/drive/1UQ9tc9AaVNd7WtJUnMArlHDBSayfozb8#" id="private-outputs-notebook-info-link" command="notebook-settings" aria-describedby="private-outputs-notebook-info-link-tooltip">Notebook settings</a><colab-tooltip-trigger aria-hidden="true" for="private-outputs-notebook-info-link" id="private-outputs-notebook-info-link-tooltip"><template shadowrootmode="open"><!----><!--?lit$571398431$--><!----><div><!--?lit$571398431$-->Open notebook settings</div><!----><!--?--></template>
        </colab-tooltip-trigger>.
          <mwc-icon-button class="close" icon="close" title="Close"><template shadowrootmode="open"><!----><button class="mdc-icon-button mdc-icon-button--display-flex" aria-label="Close"><!--?lit$571398431$-->
    <!--?lit$571398431$--><i class="material-icons"><!--?lit$571398431$-->close</i>
    <span><slot></slot></span>
  </button></template></mwc-icon-button></div>
        

    <div id="header" class="horizontal layout">
      <div id="header-background"><div></div></div>
      <div id="header-content">
        <!--?lit$571398431$-->
        <!--?lit$571398431$--><div id="header-logo">
              <!--?lit$571398431$--> <!--?lit$571398431$--><a href="https://drive.google.com/drive/search?q=owner%3Ame%20(type%3Aapplication%2Fvnd.google.colaboratory%20%7C%7C%20type%3Aapplication%2Fvnd.google.colab)&amp;authuser=0" aria-label="View in Google Drive">
        <!--?lit$571398431$--><md-icon class="colab-large-icon" aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$571398431$--><svg viewBox="0 0 24 24"><!--?lit$571398431$-->
      <g id="colab-logo">
        <path d="M4.54,9.46,2.19,7.1a6.93,6.93,0,0,0,0,9.79l2.36-2.36A3.59,3.59,0,0,1,4.54,9.46Z" style="fill:var(--colab-logo-dark)"></path>
        <path d="M2.19,7.1,4.54,9.46a3.59,3.59,0,0,1,5.08,0l1.71-2.93h0l-.1-.08h0A6.93,6.93,0,0,0,2.19,7.1Z" style="fill:var(--colab-logo-light)"></path>
        <path d="M11.34,17.46h0L9.62,14.54a3.59,3.59,0,0,1-5.08,0L2.19,16.9a6.93,6.93,0,0,0,9,.65l.11-.09" style="fill:var(--colab-logo-light)"></path>
        <path d="M12,7.1a6.93,6.93,0,0,0,0,9.79l2.36-2.36a3.59,3.59,0,1,1,5.08-5.08L21.81,7.1A6.93,6.93,0,0,0,12,7.1Z" style="fill:var(--colab-logo-light)"></path>
        <path d="M21.81,7.1,19.46,9.46a3.59,3.59,0,0,1-5.08,5.08L12,16.9A6.93,6.93,0,0,0,21.81,7.1Z" style="fill:var(--colab-logo-dark)"></path>
      </g></svg></md-icon>
      </a><!--?-->
            </div>
        <div id="header-doc-toolbar" class="flex">
          <div id="document-info">
            <!--?lit$571398431$--> <!--?lit$571398431$--><md-icon class="file-location-icon" id="file-type" aria-hidden="true" title="Notebook stored in Google Drive"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$571398431$-->
      <svg viewBox="0 0 192 192">
        <path d="M128.33,122l7.59,26.17l19.89,21.42c0,0,0,0,0,0v0c2.69-1.55,4.98-3.8,6.59-6.59l18.48-32 c1.61-2.78,2.41-5.89,2.41-9l-28.38-5.5L128.33,122z" fill="#EA4335"></path>
        <path d="M123.48,18.41c-2.69-1.55-5.78-2.41-9-2.41H77.53c-3.2,0-6.32,0.88-9,2.41l0,0l7.96,26.81l19.44,20.64 L96,66l0,0l19.58-20.89L123.48,18.41C123.48,18.41,123.48,18.41,123.48,18.41C123.48,18.41,123.48,18.41,123.48,18.41z" fill="#188038"></path>
        <path d="M63.67,122l-28.33-6.5L8.72,122c0,3.1,0.8,6.2,2.4,8.99L29.6,163c1.61,2.78,3.9,5.03,6.59,6.59 l19.59-20.18L63.67,122L63.67,122z" fill="#1967D2"></path>
        <path d="M155.47,69l-25.4-44c-1.61-2.79-3.9-5.04-6.59-6.59L96,66l32.33,56h54.95c0-3.11-0.8-6.21-2.41-9 L155.47,69z" fill="#FBBC04"></path><path d="M128.33,122H63.67l-27.48,47.59c2.69,1.55,5.78,2.41,9,2.41h101.61c3.22,0,6.31-0.86,9-2.41L128.33,122z" fill="#4285F4"></path>
        <path d="M96,66L68.53,18.41c-2.69,1.55-4.97,3.79-6.58,6.57l-50.83,88.05c-1.6,2.78-2.4,5.88-2.4,8.97h54.95L96,66 z" fill="#34A853"></path>
      </svg></md-icon>
    <input id="doc-name" class="doc-name" maxlength="259" autocomplete="off" aria-label="Notebook name" command="rename" aria-describedby="doc-name-tooltip" fdprocessedid="83vwhl" style="width: 361.156px;"><colab-tooltip-trigger aria-hidden="true" for="doc-name" id="doc-name-tooltip"><template shadowrootmode="open"><!----><!--?lit$571398431$--><!----><div><!--?lit$571398431$-->Rename notebook</div><!----><!--?--></template>
        </colab-tooltip-trigger><colab-input-sizer aria-hidden="true" style="left: -1000%; position: absolute; font-family: &quot;Google Sans&quot;, Roboto, Noto, sans-serif; font-size: 18px; font-weight: 400; letter-spacing: normal; padding-left: 3px; padding-right: 4px; white-space: pre;">Task 1 - Chatbot with Rule-based responses_</colab-input-sizer>
            <!--?lit$571398431$-->
                  <div class="screenreader-only" id="star-status" aria-live="polite">Notebook unstarred</div>
                  <md-icon-button id="star-icon" command="toggle-star" aria-describedby="star-icon-tooltip" data-aria-label="Star" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Star">
        <!--?lit$571398431$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$571398431$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface"></div></template></md-ripple>
        <!--?lit$571398431$--><span class="icon"><slot></slot></span>
        <!--?lit$571398431$-->
        <!--?lit$571398431$--><span class="touch"></span>
        <!--?lit$571398431$-->
  </button></template>
                    <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>star</md-icon>
                  </md-icon-button><colab-tooltip-trigger aria-hidden="true" for="star-icon" id="star-icon-tooltip"><template shadowrootmode="open"><!----><!--?lit$571398431$--><!----><div><!--?lit$571398431$-->Star notebook in Google Drive</div><!----><!--?--></template>
        </colab-tooltip-trigger>
                
          </div>
        <div class="menubar-wrapper"><div><!----><div id="top-menubar" class="goog-menubar format-lightborder" role="menubar" tabindex="0" style="user-select: none;" aria-activedescendant="download-submenu-menu-button"><!--?lit$571398431$--><div class="goog-menu-button goog-inline-block" id="file-menu-button" role="button" aria-expanded="false" aria-haspopup="true" style="user-select: none;"><div class="goog-inline-block goog-menu-button-outer-box" style="user-select: none;"><div class="goog-inline-block goog-menu-button-inner-box" style="user-select: none;"><div class="goog-inline-block goog-menu-button-caption" style="user-select: none;"><!--?lit$571398431$-->File</div><div class="goog-inline-block goog-menu-button-dropdown" style="user-select: none;">&nbsp;</div></div></div></div><div class="goog-menu-button goog-inline-block" id="edit-menu-button" role="button" aria-expanded="false" aria-haspopup="true" style="user-select: none;"><div class="goog-inline-block goog-menu-button-outer-box" style="user-select: none;"><div class="goog-inline-block goog-menu-button-inner-box" style="user-select: none;"><div class="goog-inline-block goog-menu-button-caption" style="user-select: none;"><!--?lit$571398431$-->Edit</div><div class="goog-inline-block goog-menu-button-dropdown" style="user-select: none;">&nbsp;</div></div></div></div><div class="goog-menu-button goog-inline-block" id="view-menu-button" role="button" aria-expanded="false" aria-haspopup="true" style="user-select: none;"><div class="goog-inline-block goog-menu-button-outer-box" style="user-select: none;"><div class="goog-inline-block goog-menu-button-inner-box" style="user-select: none;"><div class="goog-inline-block goog-menu-button-caption" style="user-select: none;"><!--?lit$571398431$-->View</div><div class="goog-inline-block goog-menu-button-dropdown" style="user-select: none;">&nbsp;</div></div></div></div><div class="goog-menu-button goog-inline-block" id="insert-menu-button" role="button" aria-expanded="false" aria-haspopup="true" style="user-select: none;"><div class="goog-inline-block goog-menu-button-outer-box" style="user-select: none;"><div class="goog-inline-block goog-menu-button-inner-box" style="user-select: none;"><div class="goog-inline-block goog-menu-button-caption" style="user-select: none;"><!--?lit$571398431$-->Insert</div><div class="goog-inline-block goog-menu-button-dropdown" style="user-select: none;">&nbsp;</div></div></div></div><div class="goog-menu-button goog-inline-block" id="runtime-menu-button" role="button" aria-expanded="false" aria-haspopup="true" style="user-select: none;"><div class="goog-inline-block goog-menu-button-outer-box" style="user-select: none;"><div class="goog-inline-block goog-menu-button-inner-box" style="user-select: none;"><div class="goog-inline-block goog-menu-button-caption" style="user-select: none;"><!--?lit$571398431$-->Runtime</div><div class="goog-inline-block goog-menu-button-dropdown" style="user-select: none;">&nbsp;</div></div></div></div><div class="goog-menu-button goog-inline-block" id="tools-menu-button" role="button" aria-expanded="false" aria-haspopup="true" style="user-select: none;"><div class="goog-inline-block goog-menu-button-outer-box" style="user-select: none;"><div class="goog-inline-block goog-menu-button-inner-box" style="user-select: none;"><div class="goog-inline-block goog-menu-button-caption" style="user-select: none;"><!--?lit$571398431$-->Tools</div><div class="goog-inline-block goog-menu-button-dropdown" style="user-select: none;">&nbsp;</div></div></div></div><div class="goog-menu-button goog-inline-block" id="help-menu-button" role="button" aria-expanded="false" aria-haspopup="true" style="user-select: none;"><div class="goog-inline-block goog-menu-button-outer-box" style="user-select: none;"><div class="goog-inline-block goog-menu-button-inner-box" style="user-select: none;"><div class="goog-inline-block goog-menu-button-caption" style="user-select: none;"><!--?lit$571398431$-->Help</div><div class="goog-inline-block goog-menu-button-dropdown" style="user-select: none;">&nbsp;</div></div></div></div></div>
    <div id="colab-menu-cover" style="left: 65px; top: 60px; width: 33px; display: none;"> </div></div><!----><colab-last-saved-indicator aria-live="polite" aria-atomic="true" title=""><template shadowrootmode="open"><!----><button class=" save-message "><!--?lit$571398431$-->All changes saved</button></template></colab-last-saved-indicator></div></div>
        <div id="header-right">
          <!--?lit$571398431$-->
    <colab-collaborator-bar id="collaborator-bar"><template shadowrootmode="open"><!----> <div class="collaborator-bar">
      <!--?lit$571398431$-->
      <!--?lit$571398431$-->
    </div></template></colab-collaborator-bar>
  
          <!--?lit$571398431$--> <md-text-button id="comments" command="open-comments-thread" aria-describedby="comments-tooltip" value="" has-icon=""><template shadowrootmode="open" shadowrootdelegatesfocus><!---->
      <!--?lit$571398431$-->
      <div class="background"></div>
      <md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
      <md-ripple part="ripple" for="button" aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface"></div></template></md-ripple>
      <!--?lit$571398431$--><button id="button" class="button">
      <!--?lit$571398431$-->
      <span class="touch"></span>
      <!--?lit$571398431$--><slot name="icon"></slot>
      <span class="label"><slot></slot></span>
      <!--?lit$571398431$-->
    
    </button>
    </template>
                <md-icon slot="icon" aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>comment</md-icon>
                <!--?lit$571398431$-->Comment
              </md-text-button><colab-tooltip-trigger aria-hidden="true" for="comments" id="comments-tooltip"><template shadowrootmode="open"><!----><!--?lit$571398431$--><!----><div><!--?lit$571398431$-->Open comments pane</div><!----><!--?--></template>
        </colab-tooltip-trigger>
          <!--?lit$571398431$--> <md-text-button id="share-toolbar-button" command="share" aria-describedby="share-toolbar-button-tooltip" value="" has-icon=""><template shadowrootmode="open" shadowrootdelegatesfocus><!---->
      <!--?lit$571398431$-->
      <div class="background"></div>
      <md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
      <md-ripple part="ripple" for="button" aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface"></div></template></md-ripple>
      <!--?lit$571398431$--><button id="button" class="button">
      <!--?lit$571398431$-->
      <span class="touch"></span>
      <!--?lit$571398431$--><slot name="icon"></slot>
      <span class="label"><slot></slot></span>
      <!--?lit$571398431$-->
    
    </button>
    </template>
                <md-icon slot="icon" aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$571398431$-->people</md-icon>
                <!--?lit$571398431$-->Share
              </md-text-button><colab-tooltip-trigger aria-hidden="true" for="share-toolbar-button" id="share-toolbar-button-tooltip"><template shadowrootmode="open"><!----><!--?lit$571398431$--><!----><div><!--?lit$571398431$-->Share notebook</div><!----><!--?--></template>
        </colab-tooltip-trigger>
          <!--?lit$571398431$--> <md-icon-button id="settings-cog" command="preferences" title="Open settings" data-aria-label="Open settings" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Open settings">
        <!--?lit$571398431$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$571398431$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface"></div></template></md-ripple>
        <!--?lit$571398431$--><span class="icon"><slot></slot></span>
        <!--?lit$571398431$-->
        <!--?lit$571398431$--><span class="touch"></span>
        <!--?lit$571398431$-->
  </button></template>
                <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>settings</md-icon>
              </md-icon-button>
          <div class="header-onegoogle-container"><div class="onegoogle"><div class="gb_ga gb_cd gb_8a gb_Rc" id="gb"><div class="gb_td gb_6a gb_hd" ng-non-bindable="" data-ogsr-up="" style="padding:0;height:auto;display:block"><div class="gb_Ld" style="display:block"><div class="gb_Xc"></div><div class="gb_b gb_Fd gb_Pf gb_z"><div class="gb_f gb_5a gb_Pf gb_z"><a class="gb_d gb_ya gb_z" aria-label="Google Account: Nithish  
(indlanithish2002@gmail.com)" href="https://accounts.google.com/SignOutOptions?hl=en&amp;continue=https://colab.research.google.com/drive/1UQ9tc9AaVNd7WtJUnMArlHDBSayfozb8&amp;ec=GBRAqQM" tabindex="0" role="button"><img class="gb_p gbii" src="./Task 1 - Chatbot with Rule-based responses_files/unnamed.jpg" srcset="https://lh3.googleusercontent.com/ogw/AF2bZyhn28GLlH5XmPF7twgtCN89mjKvnoUeWV5rAjhQy0v52kk=s32-c-mo 1x, https://lh3.googleusercontent.com/ogw/AF2bZyhn28GLlH5XmPF7twgtCN89mjKvnoUeWV5rAjhQy0v52kk=s64-c-mo 2x " alt="" aria-hidden="true" data-noaft=""></a></div></div></div><div style="overflow: hidden; position: absolute; top: 0px; visibility: hidden; width: 436px; z-index: 991; height: 0px; margin-top: 57px; right: 0px; margin-right: 4px;"></div></div></div><script nonce="">this.gbar_=this.gbar_||{};(function(_){var window=this;
try{
_.ud=function(a,b,c){if(!a.j)if(c instanceof Array)for(var d of c)_.ud(a,b,d);else{d=(0,_.z)(a.C,a,b);const e=a.v+c;a.v++;b.dataset.eqid=e;a.B[e]=d;b&&b.addEventListener?b.addEventListener(c,d,!1):b&&b.attachEvent?b.attachEvent("on"+c,d):a.o.log(Error("A`"+b))}};
}catch(e){_._DumpException(e)}
try{
_.vd=function(){if(!_.t.addEventListener||!Object.defineProperty)return!1;var a=!1,b=Object.defineProperty({},"passive",{get:function(){a=!0}});try{const c=()=>{};_.t.addEventListener("test",c,b);_.t.removeEventListener("test",c,b)}catch(c){}return a}();
}catch(e){_._DumpException(e)}
try{
var wd=document.querySelector(".gb_k .gb_d"),xd=document.querySelector("#gb.gb_Oc");wd&&!xd&&_.ud(_.ed,wd,"click");
}catch(e){_._DumpException(e)}
try{
_.xh=function(a){const b=[];let c=0;for(const d in a)b[c++]=a[d];return b};_.yh=function(a){if(a.v)return a.v;for(const b in a.i)if(a.i[b].qa()&&a.i[b].B())return a.i[b];return null};_.zh=function(a,b){a.i[b.K()]=b};var Ah=new class extends _.R{constructor(){var a=_.Oc;super();this.B=a;this.v=null;this.o={};this.C={};this.i={};this.j=null}A(a){this.i[a]&&(_.yh(this)&&_.yh(this).K()==a||this.i[a].R(!0))}Va(a){this.j=a;for(const b in this.i)this.i[b].qa()&&this.i[b].Va(a)}oc(a){return a in this.i?this.i[a]:null}};_.hd("dd",Ah);
}catch(e){_._DumpException(e)}
try{
_.Si=function(a,b){return _.M(a,36,b)};
}catch(e){_._DumpException(e)}
try{
var Ti=document.querySelector(".gb_b .gb_d"),Ui=document.querySelector("#gb.gb_Oc");Ti&&!Ui&&_.ud(_.ed,Ti,"click");
}catch(e){_._DumpException(e)}
})(this.gbar_);
// Google Inc.
</script></div></div>
        </div>
      </div>
    </div>
  </div></div><div class="notebook-horizontal">
        <!--?lit$571398431$--><colab-left-pane role="complementary" aria-label="left pane"><!----><div class="colab-left-pane-nib layout vertical" role="toolbar" aria-orientation="vertical">
        <div class="left-pane-top"><!----><div class="left-pane-button">
        <!--?lit$571398431$--><md-icon-button toggle="" command="show-toc-pane" data-aria-label="Table of contents" title="Table of contents" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Table of contents" aria-pressed="false">
        <!--?lit$571398431$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$571398431$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$571398431$--><span class="icon"><slot></slot></span>
        <!--?lit$571398431$-->
        <!--?lit$571398431$--><span class="touch"></span>
        <!--?lit$571398431$-->
  </button></template>
          <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$571398431$-->format_list_bulleted</md-icon>
        </md-icon-button> <!--?lit$571398431$-->
      </div><!----><div class="left-pane-button">
        <!--?lit$571398431$--><md-icon-button toggle="" command="find" data-aria-label="Find and replace" title="Find and replace" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Find and replace" aria-pressed="false">
        <!--?lit$571398431$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$571398431$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface"></div></template></md-ripple>
        <!--?lit$571398431$--><span class="icon"><slot></slot></span>
        <!--?lit$571398431$-->
        <!--?lit$571398431$--><span class="touch"></span>
        <!--?lit$571398431$-->
  </button></template>
          <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$571398431$-->search</md-icon>
        </md-icon-button> <!--?lit$571398431$-->
      </div><!----><div class="left-pane-button">
        <!--?lit$571398431$--><md-icon-button toggle="" command="show-variables" data-aria-label="Variables" title="Variables" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Variables" aria-pressed="false">
        <!--?lit$571398431$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$571398431$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface"></div></template></md-ripple>
        <!--?lit$571398431$--><span class="icon"><slot></slot></span>
        <!--?lit$571398431$-->
        <!--?lit$571398431$--><span class="touch"></span>
        <!--?lit$571398431$-->
  </button></template>
          <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$571398431$--><svg viewBox="0 0 24 24"><!--?lit$571398431$-->
      <path d="M4.51,9.44V6.08c0-1.34.37-1.85,1.6-2.17l.22-.06V3.13l-.27,0-.44,0a4.46,4.46,0,0,0-2.2.59,2.78,2.78,0,0,0-1,2.51V9.74c0,1.26-.26,1.61-1.49,2L0,12l.94.29c1.21.38,1.49.75,1.49,2v3.5a2.94,2.94,0,0,0,1,2.6,4.39,4.39,0,0,0,2.14.56l.46,0,.27,0v-.72l-.22-.06c-1.24-.32-1.6-.81-1.6-2.17V14.58c0-1.43-.3-2.13-1.25-2.57C4.2,11.57,4.51,10.87,4.51,9.44Z"></path>
      <path d="M23.06,11.71c-1.22-.36-1.49-.71-1.49-2l0-3.5a3,3,0,0,0-1-2.6,4.38,4.38,0,0,0-2.14-.56l-.46,0-.27,0v.72l.22.06c1.24.32,1.6.81,1.6,2.17V9.44c0,1.44.3,2.13,1.25,2.57-1,.44-1.25,1.14-1.25,2.57v3.36c0,1.34-.37,1.85-1.6,2.17l-.22.06v.72l.27,0,.44,0a4.47,4.47,0,0,0,2.2-.59,2.82,2.82,0,0,0,1-2.51V14.28c0-1.26.26-1.61,1.49-2L24,12Z"></path>
      <path d="M15.16,8.22a.88.88,0,0,1,.46.16,1.25,1.25,0,0,0,.69.2h0A1,1,0,0,0,17,8.23a1.06,1.06,0,0,0,.24-.8,1.1,1.1,0,0,0-1.15-1h0c-1,0-1.73.64-3,2.57l-.12-.51c-.28-1.36-.56-2-1.39-2h0A8,8,0,0,0,9,7.08l-.47.16.16.91L9.41,8a3.22,3.22,0,0,1,.73-.14c.34,0,.43,0,.71,1.2l.56,2.47L9.76,13.82a3.6,3.6,0,0,1-.8.88.9.9,0,0,1-.38-.13,1.83,1.83,0,0,0-.88-.28,1,1,0,0,0-1,1.06A1.15,1.15,0,0,0,8,16.53c.85,0,1.35-.35,2.24-1.55l1.49-2,.46,1.88c.23,1,.46,1.66,1.53,1.66s1.66-.75,2.81-2.53l.17-.26-.81-.48-.16.2-.25.34-.19.25c-.45.57-.62.73-.76.73s-.28-.4-.34-.63l-.67-2.83a4.2,4.2,0,0,1-.15-.79C13.84,9.78,14.74,8.22,15.16,8.22Z"></path></svg></md-icon>
        </md-icon-button> <!--?lit$571398431$-->
      </div><!----><div class="left-pane-button">
        <!--?lit$571398431$--><md-icon-button toggle="" command="open-user-secrets" data-aria-label="Secrets" title="Secrets" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Secrets" aria-pressed="false">
        <!--?lit$571398431$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$571398431$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface"></div></template></md-ripple>
        <!--?lit$571398431$--><span class="icon"><slot></slot></span>
        <!--?lit$571398431$-->
        <!--?lit$571398431$--><span class="touch"></span>
        <!--?lit$571398431$-->
  </button></template>
          <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$571398431$-->vpn_key</md-icon>
        </md-icon-button> <!--?lit$571398431$-->
      </div><!----><div class="left-pane-button">
        <!--?lit$571398431$--><md-icon-button toggle="" command="show-files" data-aria-label="Files" title="Files" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Files" aria-pressed="false">
        <!--?lit$571398431$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$571398431$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$571398431$--><span class="icon"><slot></slot></span>
        <!--?lit$571398431$-->
        <!--?lit$571398431$--><span class="touch"></span>
        <!--?lit$571398431$-->
  </button></template>
          <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$571398431$-->folder</md-icon>
        </md-icon-button> <!--?lit$571398431$-->
      </div></div>
        <div class="left-pane-bottom"><!----><div class="left-pane-button">
        <!--?lit$571398431$--><md-icon-button command="snippets" data-aria-label="Code snippets" title="Code snippets" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Code snippets">
        <!--?lit$571398431$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$571398431$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$571398431$--><span class="icon"><slot></slot></span>
        <!--?lit$571398431$-->
        <!--?lit$571398431$--><span class="touch"></span>
        <!--?lit$571398431$-->
  </button></template>
          <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$571398431$-->code</md-icon>
        </md-icon-button> <!--?lit$571398431$-->
      </div><!----><div class="left-pane-button">
        <!--?lit$571398431$--><md-icon-button command="show-command-palette" data-aria-label="Command palette" title="Command palette" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Command palette">
        <!--?lit$571398431$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$571398431$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$571398431$--><span class="icon"><slot></slot></span>
        <!--?lit$571398431$-->
        <!--?lit$571398431$--><span class="touch"></span>
        <!--?lit$571398431$-->
  </button></template>
          <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$571398431$--><svg viewBox="0 0 24 24"><!--?lit$571398431$-->
      <path d="M21,3H3A2,2,0,0,0,1,5V17a2,2,0,0,0,2,2H21a2,2,0,0,0,2-2V5A2,2,0,0,0,21,3Zm0,2V17H3V5"></path>
      <rect x="5" y="12" width="11" height="2"></rect>
      <rect x="5" y="8" width="11" height="2"></rect>
      <rect x="17" y="8" width="2" height="2"></rect>
      <rect x="17" y="12" width="2" height="2"></rect></svg></md-icon>
        </md-icon-button> <!--?lit$571398431$-->
      </div><!----><div class="left-pane-button">
        <!--?lit$571398431$--><md-icon-button command="show-terminal" data-aria-label="Terminal" title="Terminal" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Terminal">
        <!--?lit$571398431$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$571398431$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$571398431$--><span class="icon"><slot></slot></span>
        <!--?lit$571398431$-->
        <!--?lit$571398431$--><span class="touch"></span>
        <!--?lit$571398431$-->
  </button></template>
          <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$571398431$-->terminal</md-icon>
        </md-icon-button> <!--?lit$571398431$-->
      </div></div>
      </div></colab-left-pane>
        <div class="layout vertical grow">
          <colab-notebook-toolbar id="top-toolbar" class="horizontal layout center noshrink"><!----> <!--?lit$571398431$-->
          <colab-toolbar-button command="insert-cell-below" icon="add" id="toolbar-add-code"><template shadowrootmode="open"><!----><md-text-button id="button" data-aria-disabled="false" value="" has-icon=""><template shadowrootmode="open" shadowrootdelegatesfocus><!---->
      <!--?lit$571398431$-->
      <div class="background"></div>
      <md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
      <md-ripple part="ripple" for="button" aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface"></div></template></md-ripple>
      <!--?lit$571398431$--><button id="button" class="button">
      <!--?lit$571398431$-->
      <span class="touch"></span>
      <!--?lit$571398431$--><slot name="icon"></slot>
      <span class="label"><slot></slot></span>
      <!--?lit$571398431$-->
    
    </button>
    </template>
        <!--?lit$571398431$--><md-icon slot="icon" aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$571398431$-->add</md-icon>
        <span class="button-content"><slot></slot></span>
        <!--?lit$571398431$--><span class="screenreader-only"><!--?lit$571398431$-->Insert code cell below <!--?lit$571398431$-->Ctrl+M B</span>
      </md-text-button>
      <!--?lit$571398431$--> <colab-tooltip-trigger for="button" aria-hidden="true" id="tooltip" message="Insert code cell below" shortcut="Ctrl+M B"><template shadowrootmode="open"><!----><!--?lit$571398431$--><!----><div><!--?lit$571398431$-->Insert code cell below</div><!----><!--?--></template>
          </colab-tooltip-trigger><!--?--></template>
            <!--?lit$571398431$-->Code
          </colab-toolbar-button>
          <colab-toolbar-button command="add-text" icon="add" id="toolbar-add-text"><template shadowrootmode="open"><!----><md-text-button id="button" data-aria-disabled="false" value="" has-icon=""><template shadowrootmode="open" shadowrootdelegatesfocus><!---->
      <!--?lit$571398431$-->
      <div class="background"></div>
      <md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
      <md-ripple part="ripple" for="button" aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface"></div></template></md-ripple>
      <!--?lit$571398431$--><button id="button" class="button">
      <!--?lit$571398431$-->
      <span class="touch"></span>
      <!--?lit$571398431$--><slot name="icon"></slot>
      <span class="label"><slot></slot></span>
      <!--?lit$571398431$-->
    
    </button>
    </template>
        <!--?lit$571398431$--><md-icon slot="icon" aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$571398431$-->add</md-icon>
        <span class="button-content"><slot></slot></span>
        <!--?lit$571398431$--><span class="screenreader-only"><!--?lit$571398431$-->Add text cell <!--?lit$571398431$--></span>
      </md-text-button>
      <!--?lit$571398431$--> <colab-tooltip-trigger for="button" aria-hidden="true" id="tooltip" message="Add text cell" shortcut=""><template shadowrootmode="open"><!----><!--?lit$571398431$--><!----><div><!--?lit$571398431$-->Add text cell</div><!----><!--?--></template>
          </colab-tooltip-trigger><!--?--></template>
            <!--?lit$571398431$-->Text
          </colab-toolbar-button>
          <!--?lit$571398431$-->
        
    <!--?lit$571398431$-->
    <!--?lit$571398431$-->
    <!--?lit$571398431$-->
    <!--?lit$571398431$-->
    <!--?lit$571398431$--> <span class="collapsed-options">
          <colab-last-saved-indicator aria-live="polite" aria-atomic="true" title=""><template shadowrootmode="open"><!----><button class=" save-message "><!--?lit$571398431$-->All changes saved</button></template></colab-last-saved-indicator>
        </span>

    <span class="flex"></span>
    <!--?lit$571398431$--><colab-connect-warning-button><template shadowrootmode="open"><!----><!--?lit$571398431$--><!--?--><!--?--></template></colab-connect-warning-button>
    <!--?lit$571398431$--><!--?lit$571398431$--><colab-connect-button><template shadowrootmode="open"><!----> <!--?lit$571398431$--><!--?-->
      <colab-toolbar-button id="connect" tooltipid="colab-connect-tooltip" tooltiptext="Connect to a new runtime

          "><template shadowrootmode="open"><!----><md-text-button id="button" data-aria-disabled="false" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!---->
      <!--?lit$571398431$-->
      <div class="background"></div>
      <md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
      <md-ripple part="ripple" for="button" aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
      <!--?lit$571398431$--><button id="button" class="button">
      <!--?lit$571398431$-->
      <span class="touch"></span>
      <!--?lit$571398431$--><slot name="icon"></slot>
      <span class="label"><slot></slot></span>
      <!--?lit$571398431$-->
    
    </button>
    </template>
        <!--?lit$571398431$-->
        <span class="button-content"><slot></slot></span>
        <!--?lit$571398431$--><span class="screenreader-only"><!--?lit$571398431$-->Connect to a new runtime

           <!--?lit$571398431$--></span>
      </md-text-button>
      <!--?lit$571398431$--> <colab-tooltip-trigger for="button" aria-hidden="true" id="colab-connect-tooltip" message="Connect to a new runtime

          " shortcut=""><template shadowrootmode="open"><!----><!--?lit$571398431$--><!----><div><!--?lit$571398431$-->Connect to a new runtime</div><!----><!----><div><!--?lit$571398431$--></div><!----><!----><div><!--?lit$571398431$-->          </div><!----><!--?--></template>
          </colab-tooltip-trigger><!--?--></template>
        <!--?lit$571398431$-->Connect
      </colab-toolbar-button>
      <!--?lit$571398431$--> <md-icon-button id="connect-dropdown" data-aria-label="Additional connection options" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Additional connection options">
        <!--?lit$571398431$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$571398431$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$571398431$--><span class="icon"><slot></slot></span>
        <!--?lit$571398431$-->
        <!--?lit$571398431$--><span class="touch"></span>
        <!--?lit$571398431$-->
  </button></template>
        <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>arrow_drop_down</md-icon>
      </md-icon-button>
      <colab-tooltip-trigger for="connect-dropdown" id="connect-dropdown-tooltip" aria-hidden="true" message="Additional connection options"><template shadowrootmode="open"><!----><!--?lit$571398431$--><!----><div><!--?lit$571398431$-->Additional connection options</div><!----><!--?--></template>
      </colab-tooltip-trigger><!--?--></template></colab-connect-button><!--?-->
    <!--?lit$571398431$--> <span class="colab-separator"></span>
          <colab-toolbar-button command="show-chat" icon="spark"><template shadowrootmode="open"><!----><md-text-button id="button" data-aria-disabled="false" value="" has-icon=""><template shadowrootmode="open" shadowrootdelegatesfocus><!---->
      <!--?lit$571398431$-->
      <div class="background"></div>
      <md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
      <md-ripple part="ripple" for="button" aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
      <!--?lit$571398431$--><button id="button" class="button">
      <!--?lit$571398431$-->
      <span class="touch"></span>
      <!--?lit$571398431$--><slot name="icon"></slot>
      <span class="label"><slot></slot></span>
      <!--?lit$571398431$-->
    
    </button>
    </template>
        <!--?lit$571398431$--><md-icon slot="icon" aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$571398431$-->spark</md-icon>
        <span class="button-content"><slot></slot></span>
        <!--?lit$571398431$--><span class="screenreader-only"><!--?lit$571398431$--> <!--?lit$571398431$--></span>
      </md-text-button>
      <!--?lit$571398431$--><!--?--></template>
            <!--?lit$571398431$-->Gemini
          </colab-toolbar-button>
    <!--?lit$571398431$-->
    <span class="collapsed-options">
      <!--?lit$571398431$--><span class="colab-separator"></span>
      <!--?lit$571398431$--> <md-icon-button command="share" title="Share notebook" data-aria-label="Share notebook" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Share notebook">
        <!--?lit$571398431$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$571398431$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$571398431$--><span class="icon"><slot></slot></span>
        <!--?lit$571398431$-->
        <!--?lit$571398431$--><span class="touch"></span>
        <!--?lit$571398431$-->
  </button></template>
            <md-icon filled="" aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$571398431$-->people</md-icon>
          </md-icon-button><md-icon-button command="preferences" data-aria-label="Open settings" title="Open settings" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Open settings">
        <!--?lit$571398431$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$571398431$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$571398431$--><span class="icon"><slot></slot></span>
        <!--?lit$571398431$-->
        <!--?lit$571398431$--><span class="touch"></span>
        <!--?lit$571398431$-->
  </button></template>
        <md-icon filled="" aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>settings</md-icon>
      </md-icon-button>
    </span>
    <span class="colab-separator"></span>
    <!--?lit$571398431$--><md-icon-button toggle="" command="toggle-header" id="toggle-header-button" data-aria-label="Toggle header visibility" aria-describedby="toggle-header-button-tooltip" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Toggle header visibility" aria-pressed="false">
        <!--?lit$571398431$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$571398431$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$571398431$--><span class="icon"><slot></slot></span>
        <!--?lit$571398431$-->
        <!--?lit$571398431$--><span class="touch"></span>
        <!--?lit$571398431$-->
  </button></template>
    <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>expand_less</md-icon>
    <md-icon slot="selected" aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>expand_more</md-icon>
  </md-icon-button><colab-tooltip-trigger aria-hidden="true" for="toggle-header-button" id="toggle-header-button-tooltip"><template shadowrootmode="open"><!----><!--?lit$571398431$--><!----><div><!--?lit$571398431$-->Toggle header visibility</div><!----><!--?--></template>
        </colab-tooltip-trigger><!--?--></colab-notebook-toolbar><colab-tab-layout-container class="layout horizontal grow flexible-tabs"><!----> <div class="layout horizontal tab-pane-parent">
      <!--?lit$571398431$--> <div class="layout vertical tab-pane-parent">
      <!--?lit$571398431$--><colab-tab-pane class="layout vertical grow no-header focused" align="horizontal"><!----> <div class="layout vertical grow">
    <div class="tab-pane-header layout horizontal noshrink">
      <md-tabs><template shadowrootmode="open"><!---->
      <div class="tabs">
        <slot></slot>
      </div>
      <md-divider part="divider"><template shadowrootmode="open"><!----></template></md-divider>
    </template><md-primary-tab noink="" title="" aria-labelledby="tab-title-Tq9mhwzPVLJ2" class="selected-tab" tabindex="0" md-tab="" active=""><template shadowrootmode="open"><!----><div class="button" role="presentation">
      <md-focus-ring part="focus-ring" inward="" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
      <md-elevation part="elevation" aria-hidden="true"><template shadowrootmode="open"><!----><span class="shadow"></span></template></md-elevation>
      <md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
      <div role="presentation" class="content  has-label stacked ">
        <slot name="icon"></slot>
        <slot></slot>
        <!--?lit$571398431$--><div class="indicator"></div>
      </div>
      <!--?lit$571398431$-->
    </div></template>
          <div class="colab-tab-header">
            <span class="colab-tab-title" id="tab-title-Tq9mhwzPVLJ2"><!--?lit$571398431$--><!--?lit$571398431$-->Notebook<!--?--></span>
            <!--?lit$571398431$-->
          </div>
        </md-primary-tab></md-tabs>
      <div class="layout grow"></div>
      <!--?lit$571398431$--> <md-icon-button title="Show more" data-aria-label="Show more" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Show more">
        <!--?lit$571398431$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$571398431$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$571398431$--><span class="icon"><slot></slot></span>
        <!--?lit$571398431$-->
        <!--?lit$571398431$--><span class="touch"></span>
        <!--?lit$571398431$-->
  </button></template>
    <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>more_horiz</md-icon>
  </md-icon-button>
    </div>
    <div class="layout vertical grow tab-pane-container"> <colab-tab class="layout vertical grow notebook-tab-content selected-tab"><!----> <div class="overflow-flexbox-workaround">
      <colab-shaded-scroller ignore-dom-changes="" tabindex="-1" role="main" class="notebook-container" aria-label="Notebook">
        <div class="notebook-scrolling-horizontal-container">
          <div class="notebook-scrolling-horizontal">
            <div class="notebook-content-background">
              <!--?lit$571398431$-->
              <div class="notebook-content ">
                <!--?lit$571398431$--><div class="add-cell">
      <div class="add-cell-buttons">
        <md-outlined-button class="add-code add-button" data-aria-label="Add code cell
Ctrl+M B" title="Add code cell
Ctrl+M B" value="" has-icon=""><template shadowrootmode="open" shadowrootdelegatesfocus><!---->
      <!--?lit$571398431$--><div class="outline"></div>
      <div class="background"></div>
      <md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
      <md-ripple part="ripple" for="button" aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
      <!--?lit$571398431$--><button id="button" class="button" aria-label="Add code cell
Ctrl+M B">
      <!--?lit$571398431$-->
      <span class="touch"></span>
      <!--?lit$571398431$--><slot name="icon"></slot>
      <span class="label"><slot></slot></span>
      <!--?lit$571398431$-->
    
    </button>
    </template>
          <md-icon slot="icon" aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>add</md-icon>
          <!--?lit$571398431$-->Code
        </md-outlined-button>
        <md-outlined-button class="add-text add-button" data-aria-label="Add text cell" title="Add text cell" value="" has-icon=""><template shadowrootmode="open" shadowrootdelegatesfocus><!---->
      <!--?lit$571398431$--><div class="outline"></div>
      <div class="background"></div>
      <md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
      <md-ripple part="ripple" for="button" aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
      <!--?lit$571398431$--><button id="button" class="button" aria-label="Add text cell">
      <!--?lit$571398431$-->
      <span class="touch"></span>
      <!--?lit$571398431$--><slot name="icon"></slot>
      <span class="label"><slot></slot></span>
      <!--?lit$571398431$-->
    
    </button>
    </template>
          <md-icon slot="icon" aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>add</md-icon>
          <!--?lit$571398431$-->Text
        </md-outlined-button>
        <!--?lit$571398431$-->
      </div><hr>
    </div>
                <div class="notebook-cell-list"><div class="cell code code-has-output icon-scrolling focused" id="cell-NLqjQE0mVcD-" tabindex="-1" role="region" aria-label="Cell 0: Code cell: " style=""><div class="cell-tag-editor sticky"></div><div class="cell-toolbar sticky"><colab-cell-toolbar><template shadowrootmode="open"><!----><!--?lit$571398431$--><!----> <md-icon-button class="colab-icon" title="Move cell up
Ctrl+M K" data-aria-label="Move cell up
Ctrl+M K" command="move-cell-up" disabled="" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Move cell up
Ctrl+M K" disabled="">
        <!--?lit$571398431$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$571398431$--><md-ripple disabled="" aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$571398431$--><span class="icon"><slot></slot></span>
        <!--?lit$571398431$-->
        <!--?lit$571398431$--><span class="touch"></span>
        <!--?lit$571398431$-->
  </button></template>
          <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$571398431$-->arrow_upward</md-icon>
          <!--?lit$571398431$-->
        </md-icon-button><!----><!----> <md-icon-button class="colab-icon" title="Move cell down
Ctrl+M J" data-aria-label="Move cell down
Ctrl+M J" command="move-cell-down" disabled="" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Move cell down
Ctrl+M J" disabled="">
        <!--?lit$571398431$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$571398431$--><md-ripple disabled="" aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$571398431$--><span class="icon"><slot></slot></span>
        <!--?lit$571398431$-->
        <!--?lit$571398431$--><span class="touch"></span>
        <!--?lit$571398431$-->
  </button></template>
          <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$571398431$-->arrow_downward</md-icon>
          <!--?lit$571398431$-->
        </md-icon-button><!----><!----> <md-icon-button class="colab-icon" title="Copy link to cell" data-aria-label="Copy link to cell" command="copy-link-to-cell" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Copy link to cell">
        <!--?lit$571398431$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$571398431$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$571398431$--><span class="icon"><slot></slot></span>
        <!--?lit$571398431$-->
        <!--?lit$571398431$--><span class="touch"></span>
        <!--?lit$571398431$-->
  </button></template>
          <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$571398431$-->link</md-icon>
          <!--?lit$571398431$-->
        </md-icon-button><!----><!----> <md-icon-button class="colab-icon" title="Add a comment
Ctrl+Alt+M" data-aria-label="Add a comment
Ctrl+Alt+M" command="add-comment" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Add a comment
Ctrl+Alt+M">
        <!--?lit$571398431$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$571398431$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$571398431$--><span class="icon"><slot></slot></span>
        <!--?lit$571398431$-->
        <!--?lit$571398431$--><span class="touch"></span>
        <!--?lit$571398431$-->
  </button></template>
          <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$571398431$-->comment</md-icon>
          <!--?lit$571398431$-->
        </md-icon-button><!----><!----> <md-icon-button class="colab-icon" title="Open editor settings" data-aria-label="Open editor settings" command="editor-preferences" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Open editor settings">
        <!--?lit$571398431$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$571398431$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$571398431$--><span class="icon"><slot></slot></span>
        <!--?lit$571398431$-->
        <!--?lit$571398431$--><span class="touch"></span>
        <!--?lit$571398431$-->
  </button></template>
          <md-icon filled="" aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$571398431$-->settings</md-icon>
          <!--?lit$571398431$-->
        </md-icon-button><!----><!----> <md-icon-button class="colab-icon" title="Edit" data-aria-label="Edit" command="toggle-edit-markdown" toggle="" style="display: none;" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Edit" aria-pressed="false">
        <!--?lit$571398431$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$571398431$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$571398431$--><span class="icon"><slot></slot></span>
        <!--?lit$571398431$-->
        <!--?lit$571398431$--><span class="touch"></span>
        <!--?lit$571398431$-->
  </button></template>
          <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$571398431$-->edit</md-icon>
          <!--?lit$571398431$--><md-icon slot="selected" aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$571398431$-->edit_off</md-icon>
        </md-icon-button><!----><!----> <md-icon-button class="colab-icon" title="Mirror cell in tab" data-aria-label="Mirror cell in tab" command="mirror-cell-in-tab" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Mirror cell in tab">
        <!--?lit$571398431$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$571398431$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$571398431$--><span class="icon"><slot></slot></span>
        <!--?lit$571398431$-->
        <!--?lit$571398431$--><span class="touch"></span>
        <!--?lit$571398431$-->
  </button></template>
          <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$571398431$--><svg viewBox="0 0 24 24"><!--?lit$571398431$-->
      <g id="mirror-cell">
        <path d="M4,21V7H2V21a2,2,0,0,0,2,2H18V21Z"></path>
        <path d="M6,13v2H8.6L5,18.6,6.4,20,10,16.4V19h2V13Z"></path>
        <path d="M19,1H8A2,2,0,0,0,6,3v8H8V3H19V17H14v2h5a2,2,0,0,0,2-2V3A2,2,0,0,0,19,1Z"></path>
      </g></svg></md-icon>
          <!--?lit$571398431$-->
        </md-icon-button><!----><!----> <md-icon-button class="colab-icon" title="Delete cell
Ctrl+M D" data-aria-label="Delete cell
Ctrl+M D" command="delete-cell-or-selection" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Delete cell
Ctrl+M D">
        <!--?lit$571398431$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$571398431$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$571398431$--><span class="icon"><slot></slot></span>
        <!--?lit$571398431$-->
        <!--?lit$571398431$--><span class="touch"></span>
        <!--?lit$571398431$-->
  </button></template>
          <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$571398431$-->delete</md-icon>
          <!--?lit$571398431$-->
        </md-icon-button><!----><!--?lit$571398431$--><md-icon-button title="More cell actions" data-aria-label="More cell actions" class="colab-icon cell-toolbar-more" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="More cell actions">
        <!--?lit$571398431$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$571398431$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$571398431$--><span class="icon"><slot></slot></span>
        <!--?lit$571398431$-->
        <!--?lit$571398431$--><span class="touch"></span>
        <!--?lit$571398431$-->
  </button></template><md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>more_vert</md-icon>
    </md-icon-button><!--?--></template></colab-cell-toolbar></div><div class="main-content" elevation="2"><div class="cell-contents"><div class="cell-mask"></div><span class="imported-info-area"></span><div class="codecell-input-output">
      <div class="inputarea horizontal layout code">
        <div class="cell-gutter">
          <!-- Bounding range for vertical scrolling of icons -->
          <div class="cell-execution-container">
            <colab-run-button title="Run cell (Ctrl+Enter)
cell has not been executed in this session

executed by Nithish
Wednesday, July 3, 2024 (5 days ago)
executed in 10.661s" role="button" aria-label="Run cell"><template shadowrootmode="open"><!----> <div class="cell-execution focused stale">
      <div class="execution-count"><!--?lit$571398431$-->[ ]</div>
      <div class="cell-execution-indicator"> <!--?lit$571398431$-->
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24">
  <!--?lit$571398431$-->
  <mask id="playSymbolMask">
    <rect width="100%" height="100%" fill="white"></rect>
    <polygon points="10,8 17,12 10,16" fill="black"></polygon>
  </mask>
  <circle cx="12" cy="12" r="7.8" mask="url(#playSymbolMask)" id="filledCircle"></circle>
</svg> </div>
      <!--?lit$571398431$--><!--?-->
    </div></template></colab-run-button>
          </div>
        </div>
      <div class="editor flex lazy-editor" style=""><div class="editor flex monaco" data-keybinding-context="1" data-mode-id="notebook-python" style="height: 884px; --vscode-editorCodeLens-lineHeight: 16px; --vscode-editorCodeLens-fontSize: 12px; --vscode-editorCodeLens-fontFeatureSettings: &quot;liga&quot; off, &quot;calt&quot; off;"><div class="monaco-editor no-user-select  showUnused showDeprecated vs" role="code" data-uri="inmemory://model/3" style="width: 1154px; height: 884px;"><div data-mprt="3" class="overflow-guard" style="width: 1154px; height: 884px; overflow: clip;"><div class="margin" role="presentation" aria-hidden="true" style="position: absolute; contain: strict; will-change: unset; top: 0px; height: 884px; width: 6px;"><div class="glyph-margin" style="left: 0px; width: 0px; height: 884px;"></div><div class="margin-view-zones" role="presentation" aria-hidden="true" style="position: absolute;"></div><div class="margin-view-overlays" role="presentation" aria-hidden="true" style="position: absolute; font-family: monospace, Consolas, &quot;Courier New&quot;, monospace; font-weight: normal; font-size: 14px; font-feature-settings: &quot;liga&quot; 0, &quot;calt&quot; 0; font-variation-settings: normal; line-height: 19px; letter-spacing: 0px; width: 6px; height: 884px;"><div style="position:absolute;top:0px;width:100%;height:19px;"><div class="current-line current-line-margin-both" style="width:6px; height:19px;"></div></div><div style="position:absolute;top:19px;width:100%;height:19px;"></div><div style="position:absolute;top:38px;width:100%;height:19px;"></div><div style="position:absolute;top:57px;width:100%;height:19px;"></div><div style="position:absolute;top:76px;width:100%;height:19px;"></div><div style="position:absolute;top:95px;width:100%;height:19px;"></div><div style="position:absolute;top:114px;width:100%;height:19px;"></div><div style="position:absolute;top:133px;width:100%;height:19px;"></div><div style="position:absolute;top:152px;width:100%;height:19px;"></div><div style="position:absolute;top:171px;width:100%;height:19px;"></div><div style="position:absolute;top:190px;width:100%;height:19px;"></div><div style="position:absolute;top:209px;width:100%;height:19px;"></div><div style="position:absolute;top:228px;width:100%;height:19px;"></div><div style="position:absolute;top:247px;width:100%;height:19px;"></div><div style="position:absolute;top:266px;width:100%;height:19px;"></div><div style="position:absolute;top:285px;width:100%;height:19px;"></div><div style="position:absolute;top:304px;width:100%;height:19px;"></div><div style="position:absolute;top:323px;width:100%;height:19px;"></div><div style="position:absolute;top:342px;width:100%;height:19px;"></div><div style="position:absolute;top:361px;width:100%;height:19px;"></div><div style="position:absolute;top:380px;width:100%;height:19px;"></div><div style="position:absolute;top:399px;width:100%;height:19px;"></div><div style="position:absolute;top:418px;width:100%;height:19px;"></div><div style="position:absolute;top:437px;width:100%;height:19px;"></div><div style="position:absolute;top:456px;width:100%;height:19px;"></div><div style="position:absolute;top:475px;width:100%;height:19px;"></div><div style="position:absolute;top:494px;width:100%;height:19px;"></div><div style="position:absolute;top:513px;width:100%;height:19px;"></div><div style="position:absolute;top:532px;width:100%;height:19px;"></div><div style="position:absolute;top:551px;width:100%;height:19px;"></div><div style="position:absolute;top:570px;width:100%;height:19px;"></div><div style="position:absolute;top:589px;width:100%;height:19px;"></div><div style="position:absolute;top:608px;width:100%;height:19px;"></div><div style="position:absolute;top:627px;width:100%;height:19px;"></div><div style="position:absolute;top:646px;width:100%;height:19px;"></div><div style="position:absolute;top:665px;width:100%;height:19px;"></div><div style="position:absolute;top:684px;width:100%;height:19px;"></div><div style="position:absolute;top:703px;width:100%;height:19px;"></div><div style="position:absolute;top:722px;width:100%;height:19px;"></div><div style="position:absolute;top:741px;width:100%;height:19px;"></div><div style="position:absolute;top:760px;width:100%;height:19px;"></div><div style="position:absolute;top:779px;width:100%;height:19px;"></div><div style="position:absolute;top:798px;width:100%;height:19px;"></div><div style="position:absolute;top:817px;width:100%;height:19px;"></div><div style="position:absolute;top:836px;width:100%;height:19px;"></div><div style="position:absolute;top:855px;width:100%;height:19px;"></div></div><div class="glyph-margin-widgets" style="position: absolute; top: 0px;"></div></div><div class="monaco-scrollable-element editor-scrollable vs" role="presentation" data-mprt="5" style="position: absolute; overflow: hidden; left: 6px; width: 1148px; height: 884px;"><div class="lines-content monaco-editor-background" style="position: absolute; overflow: hidden; width: 1e+06px; height: 884px; contain: strict; will-change: unset; top: 0px; left: 0px;"><div class="view-overlays" role="presentation" aria-hidden="true" style="position: absolute; font-family: monospace, Consolas, &quot;Courier New&quot;, monospace; font-weight: normal; font-size: 14px; font-feature-settings: &quot;liga&quot; 0, &quot;calt&quot; 0; font-variation-settings: normal; line-height: 19px; letter-spacing: 0px; height: 0px; width: 1148px;"><div style="position:absolute;top:0px;width:100%;height:19px;"><div class="current-line" style="width:1148px; height:19px;"></div></div><div style="position:absolute;top:19px;width:100%;height:19px;"></div><div style="position:absolute;top:38px;width:100%;height:19px;"></div><div style="position:absolute;top:57px;width:100%;height:19px;"></div><div style="position:absolute;top:76px;width:100%;height:19px;"></div><div style="position:absolute;top:95px;width:100%;height:19px;"></div><div style="position:absolute;top:114px;width:100%;height:19px;"></div><div style="position:absolute;top:133px;width:100%;height:19px;"></div><div style="position:absolute;top:152px;width:100%;height:19px;"></div><div style="position:absolute;top:171px;width:100%;height:19px;"></div><div style="position:absolute;top:190px;width:100%;height:19px;"></div><div style="position:absolute;top:209px;width:100%;height:19px;"></div><div style="position:absolute;top:228px;width:100%;height:19px;"></div><div style="position:absolute;top:247px;width:100%;height:19px;"></div><div style="position:absolute;top:266px;width:100%;height:19px;"></div><div style="position:absolute;top:285px;width:100%;height:19px;"></div><div style="position:absolute;top:304px;width:100%;height:19px;"></div><div style="position:absolute;top:323px;width:100%;height:19px;"></div><div style="position:absolute;top:342px;width:100%;height:19px;"></div><div style="position:absolute;top:361px;width:100%;height:19px;"></div><div style="position:absolute;top:380px;width:100%;height:19px;"></div><div style="position:absolute;top:399px;width:100%;height:19px;"></div><div style="position:absolute;top:418px;width:100%;height:19px;"></div><div style="position:absolute;top:437px;width:100%;height:19px;"></div><div style="position:absolute;top:456px;width:100%;height:19px;"></div><div style="position:absolute;top:475px;width:100%;height:19px;"></div><div style="position:absolute;top:494px;width:100%;height:19px;"></div><div style="position:absolute;top:513px;width:100%;height:19px;"></div><div style="position:absolute;top:532px;width:100%;height:19px;"></div><div style="position:absolute;top:551px;width:100%;height:19px;"></div><div style="position:absolute;top:570px;width:100%;height:19px;"></div><div style="position:absolute;top:589px;width:100%;height:19px;"></div><div style="position:absolute;top:608px;width:100%;height:19px;"></div><div style="position:absolute;top:627px;width:100%;height:19px;"></div><div style="position:absolute;top:646px;width:100%;height:19px;"></div><div style="position:absolute;top:665px;width:100%;height:19px;"></div><div style="position:absolute;top:684px;width:100%;height:19px;"></div><div style="position:absolute;top:703px;width:100%;height:19px;"></div><div style="position:absolute;top:722px;width:100%;height:19px;"></div><div style="position:absolute;top:741px;width:100%;height:19px;"></div><div style="position:absolute;top:760px;width:100%;height:19px;"></div><div style="position:absolute;top:779px;width:100%;height:19px;"></div><div style="position:absolute;top:798px;width:100%;height:19px;"></div><div style="position:absolute;top:817px;width:100%;height:19px;"></div><div style="position:absolute;top:836px;width:100%;height:19px;"></div><div style="position:absolute;top:855px;width:100%;height:19px;"></div></div><div role="presentation" aria-hidden="true" class="view-rulers"><div class="view-ruler" style="width: 2px; height: 884px; left: 615.938px;"></div></div><div class="view-zones" role="presentation" aria-hidden="true" style="position: absolute;"></div><div class="view-lines monaco-mouse-cursor-text" role="presentation" aria-hidden="true" data-mprt="7" style="position: absolute; font-family: monospace, Consolas, &quot;Courier New&quot;, monospace; font-weight: normal; font-size: 14px; font-feature-settings: &quot;liga&quot; 0, &quot;calt&quot; 0; font-variation-settings: normal; line-height: 19px; letter-spacing: 0px; width: 1148px; height: 884px;"><div style="top:0px;height:19px;" class="view-line"><span><span class="mtk19">import</span><span class="mtk1">&nbsp;random</span></span></div><div style="top:19px;height:19px;" class="view-line"><span><span></span></span></div><div style="top:38px;height:19px;" class="view-line"><span><span class="mtk8">#&nbsp;Define&nbsp;a&nbsp;function&nbsp;to&nbsp;get&nbsp;a&nbsp;response&nbsp;from&nbsp;the&nbsp;bot</span></span></div><div style="top:57px;height:19px;" class="view-line"><span><span class="mtk6">def</span><span class="mtk1">&nbsp;</span><span class="mtk15">get_response</span><span class="mtk1 bracket-highlighting-0">(</span><span class="mtk16">user_input</span><span class="mtk1 bracket-highlighting-0">)</span><span class="mtk1">:</span></span></div><div style="top:76px;height:19px;" class="view-line"><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="mtk8">#&nbsp;Convert&nbsp;user&nbsp;input&nbsp;to&nbsp;lowercase&nbsp;for&nbsp;case-insensi</span><span class="mtk8">tive&nbsp;matching</span></span></div><div style="top:95px;height:19px;" class="view-line"><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;user_input&nbsp;=&nbsp;user_input.lower</span><span class="mtk1 bracket-highlighting-0">(</span><span class="mtk1 bracket-highlighting-0">)</span></span></div><div style="top:114px;height:19px;" class="view-line"><span><span></span></span></div><div style="top:133px;height:19px;" class="view-line"><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="mtk8">#&nbsp;Define&nbsp;some&nbsp;basic&nbsp;rules&nbsp;and&nbsp;responses</span></span></div><div style="top:152px;height:19px;" class="view-line"><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;responses&nbsp;=&nbsp;</span><span class="mtk1 bracket-highlighting-0">{</span></span></div><div style="top:171px;height:19px;" class="view-line"><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="mtk26">'hello'</span><span class="mtk1">:&nbsp;</span><span class="mtk26">'Hello!&nbsp;How&nbsp;can&nbsp;I&nbsp;help&nbsp;you?'</span><span class="mtk1">,</span></span></div><div style="top:190px;height:19px;" class="view-line"><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="mtk26">'hi'</span><span class="mtk1">:&nbsp;</span><span class="mtk26">'Hi&nbsp;there!&nbsp;What&nbsp;can&nbsp;I&nbsp;do&nbsp;for&nbsp;you?'</span><span class="mtk1">,</span></span></div><div style="top:209px;height:19px;" class="view-line"><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="mtk26">'how&nbsp;are&nbsp;you'</span><span class="mtk1">:&nbsp;</span><span class="mtk26">'I&nbsp;am&nbsp;just&nbsp;a&nbsp;bot&nbsp;and&nbsp;don\'t&nbsp;have&nbsp;feelings,&nbsp;but&nbsp;tha</span><span class="mtk26">nks&nbsp;for&nbsp;asking!'</span><span class="mtk1">,</span></span></div><div style="top:228px;height:19px;" class="view-line"><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="mtk26">'bye'</span><span class="mtk1">:&nbsp;</span><span class="mtk26">'Goodbye!&nbsp;Have&nbsp;a&nbsp;nice&nbsp;day.'</span><span class="mtk1">,</span></span></div><div style="top:247px;height:19px;" class="view-line"><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="mtk26">'thank&nbsp;you'</span><span class="mtk1">:&nbsp;</span><span class="mtk26">'You\'re&nbsp;welcome!'</span><span class="mtk1">,</span></span></div><div style="top:266px;height:19px;" class="view-line"><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="mtk26">'default'</span><span class="mtk1">:&nbsp;</span><span class="mtk26">'I\'m&nbsp;sorry,&nbsp;I&nbsp;didn\'t&nbsp;understand&nbsp;that.'</span></span></div><div style="top:285px;height:19px;" class="view-line"><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="mtk1 bracket-highlighting-0">}</span></span></div><div style="top:304px;height:19px;" class="view-line"><span><span></span></span></div><div style="top:323px;height:19px;" class="view-line"><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="mtk8">#&nbsp;Check&nbsp;for&nbsp;specific&nbsp;user&nbsp;inputs&nbsp;and&nbsp;provide&nbsp;corre</span><span class="mtk8">sponding&nbsp;responses</span></span></div><div style="top:342px;height:19px;" class="view-line"><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="mtk19">if</span><span class="mtk1">&nbsp;user_input&nbsp;</span><span class="mtk6">in</span><span class="mtk1">&nbsp;responses:</span></span></div><div style="top:361px;height:19px;" class="view-line"><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="mtk19">return</span><span class="mtk1">&nbsp;responses</span><span class="mtk1 bracket-highlighting-0">[</span><span class="mtk1">user_input</span><span class="mtk1 bracket-highlighting-0">]</span></span></div><div style="top:380px;height:19px;" class="view-line"><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="mtk19">elif</span><span class="mtk1">&nbsp;</span><span class="mtk26">'help'</span><span class="mtk1">&nbsp;</span><span class="mtk6">in</span><span class="mtk1">&nbsp;user_input:</span></span></div><div style="top:399px;height:19px;" class="view-line"><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="mtk19">return</span><span class="mtk1">&nbsp;</span><span class="mtk26">'Sure,&nbsp;I&nbsp;can&nbsp;help.&nbsp;What&nbsp;do&nbsp;you&nbsp;need&nbsp;assistance&nbsp;wit</span><span class="mtk26">h?'</span></span></div><div style="top:418px;height:19px;" class="view-line"><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="mtk19">elif</span><span class="mtk1">&nbsp;</span><span class="mtk26">'order'</span><span class="mtk1">&nbsp;</span><span class="mtk6">in</span><span class="mtk1">&nbsp;user_input&nbsp;</span><span class="mtk6">or</span><span class="mtk1">&nbsp;</span><span class="mtk26">'buy'</span><span class="mtk1">&nbsp;</span><span class="mtk6">in</span><span class="mtk1">&nbsp;user_input:</span></span></div><div style="top:437px;height:19px;" class="view-line"><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="mtk19">return</span><span class="mtk1">&nbsp;</span><span class="mtk26">'Please&nbsp;visit&nbsp;our&nbsp;website&nbsp;to&nbsp;place&nbsp;an&nbsp;order.'</span></span></div><div style="top:456px;height:19px;" class="view-line"><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="mtk19">elif</span><span class="mtk1">&nbsp;</span><span class="mtk26">'information'</span><span class="mtk1">&nbsp;</span><span class="mtk6">in</span><span class="mtk1">&nbsp;user_input&nbsp;</span><span class="mtk6">or</span><span class="mtk1">&nbsp;</span><span class="mtk26">'info'</span><span class="mtk1">&nbsp;</span><span class="mtk6">in</span><span class="mtk1">&nbsp;user_input:</span></span></div><div style="top:475px;height:19px;" class="view-line"><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="mtk19">return</span><span class="mtk1">&nbsp;</span><span class="mtk26">'You&nbsp;can&nbsp;find&nbsp;more&nbsp;information&nbsp;on&nbsp;our&nbsp;website.'</span></span></div><div style="top:494px;height:19px;" class="view-line"><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="mtk19">else</span><span class="mtk1">:</span></span></div><div style="top:513px;height:19px;" class="view-line"><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="mtk19">return</span><span class="mtk1">&nbsp;responses</span><span class="mtk1 bracket-highlighting-0">[</span><span class="mtk26">'default'</span><span class="mtk1 bracket-highlighting-0">]</span></span></div><div style="top:532px;height:19px;" class="view-line"><span><span></span></span></div><div style="top:551px;height:19px;" class="view-line"><span><span class="mtk8">#&nbsp;Main&nbsp;function&nbsp;to&nbsp;run&nbsp;the&nbsp;chatbot</span></span></div><div style="top:570px;height:19px;" class="view-line"><span><span class="mtk6">def</span><span class="mtk1">&nbsp;</span><span class="mtk15">main</span><span class="mtk1 bracket-highlighting-0">(</span><span class="mtk1 bracket-highlighting-0">)</span><span class="mtk1">:</span></span></div><div style="top:589px;height:19px;" class="view-line"><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="mtk15">print</span><span class="mtk1 bracket-highlighting-0">(</span><span class="mtk26">"Welcome&nbsp;to&nbsp;the&nbsp;Rule-Based&nbsp;Chatbot!"</span><span class="mtk1 bracket-highlighting-0">)</span></span></div><div style="top:608px;height:19px;" class="view-line"><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="mtk15">print</span><span class="mtk1 bracket-highlighting-0">(</span><span class="mtk26">"You&nbsp;can&nbsp;start&nbsp;chatting&nbsp;with&nbsp;the&nbsp;bot.&nbsp;Type&nbsp;'bye'&nbsp;t</span><span class="mtk26">o&nbsp;exit."</span><span class="mtk1 bracket-highlighting-0">)</span></span></div><div style="top:627px;height:19px;" class="view-line"><span><span></span></span></div><div style="top:646px;height:19px;" class="view-line"><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="mtk19">while</span><span class="mtk1">&nbsp;</span><span class="mtk6">True</span><span class="mtk1">:</span></span></div><div style="top:665px;height:19px;" class="view-line"><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;user_input&nbsp;=&nbsp;</span><span class="mtk15">input</span><span class="mtk1 bracket-highlighting-0">(</span><span class="mtk26">"You:&nbsp;"</span><span class="mtk1 bracket-highlighting-0">)</span></span></div><div style="top:684px;height:19px;" class="view-line"><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="mtk19">if</span><span class="mtk1">&nbsp;user_input.lower</span><span class="mtk1 bracket-highlighting-0">(</span><span class="mtk1 bracket-highlighting-0">)</span><span class="mtk1">&nbsp;==&nbsp;</span><span class="mtk26">'bye'</span><span class="mtk1">:</span></span></div><div style="top:703px;height:19px;" class="view-line"><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="mtk15">print</span><span class="mtk1 bracket-highlighting-0">(</span><span class="mtk26">"Bot:&nbsp;Goodbye!"</span><span class="mtk1 bracket-highlighting-0">)</span></span></div><div style="top:722px;height:19px;" class="view-line"><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="mtk19">break</span></span></div><div style="top:741px;height:19px;" class="view-line"><span><span></span></span></div><div style="top:760px;height:19px;" class="view-line"><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;response&nbsp;=&nbsp;get_response</span><span class="mtk1 bracket-highlighting-0">(</span><span class="mtk1">user_input</span><span class="mtk1 bracket-highlighting-0">)</span></span></div><div style="top:779px;height:19px;" class="view-line"><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="mtk15">print</span><span class="mtk1 bracket-highlighting-0">(</span><span class="mtk26">"Bot:"</span><span class="mtk1">,&nbsp;response</span><span class="mtk1 bracket-highlighting-0">)</span></span></div><div style="top:798px;height:19px;" class="view-line"><span><span></span></span></div><div style="top:817px;height:19px;" class="view-line"><span><span class="mtk19">if</span><span class="mtk1">&nbsp;</span><span class="mtk16">__name__</span><span class="mtk1">&nbsp;==&nbsp;</span><span class="mtk26">"__main__"</span><span class="mtk1">:</span></span></div><div style="top:836px;height:19px;" class="view-line"><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;main</span><span class="mtk1 bracket-highlighting-0">(</span><span class="mtk1 bracket-highlighting-0">)</span></span></div><div style="top:855px;height:19px;" class="view-line"><span><span></span></span></div></div><div data-mprt="1" class="contentWidgets" style="position: absolute; top: 0px;"></div><div role="presentation" aria-hidden="true" class="cursors-layer cursor-line-style cursor-solid"><div class="cursor monaco-mouse-cursor-text " style="height: 19px; top: 0px; left: 0px; font-family: monospace, Consolas, &quot;Courier New&quot;, monospace; font-weight: normal; font-size: 14px; font-feature-settings: &quot;liga&quot; 0, &quot;calt&quot; 0; font-variation-settings: normal; line-height: 19px; letter-spacing: 0px; display: block; visibility: hidden; padding-left: 0px; width: 2px;"></div></div></div><div role="presentation" aria-hidden="true" class="invisible scrollbar horizontal" style="position: absolute; width: 1134px; height: 10px; left: 0px; bottom: 0px;"><div class="slider" style="position: absolute; top: 0px; left: 0px; height: 10px; transform: translate3d(0px, 0px, 0px); contain: strict; will-change: unset; width: 1134px;"></div></div><canvas class="decorationsOverviewRuler" aria-hidden="true" width="21" height="1326" style="position: absolute; transform: translate3d(0px, 0px, 0px); contain: strict; top: 0px; right: 0px; width: 14px; height: 884px; will-change: unset; display: block;"></canvas><div role="presentation" aria-hidden="true" class="invisible scrollbar vertical" style="position: absolute; width: 14px; height: 884px; right: 0px; top: 0px;"><div class="slider" style="position: absolute; top: 0px; left: 0px; width: 14px; transform: translate3d(0px, 0px, 0px); contain: strict; will-change: unset; height: 884px;"></div></div></div><div role="presentation" aria-hidden="true" style="width: 1154px;"></div><textarea data-mprt="6" class="inputarea monaco-mouse-cursor-text" wrap="on" autocorrect="off" autocapitalize="off" autocomplete="off" spellcheck="false" aria-label="Editor content;Press Alt+F1 for Accessibility Options." tabindex="0" role="textbox" aria-roledescription="editor" aria-multiline="true" aria-haspopup="false" aria-autocomplete="both" style="tab-size: 15.3984px; font-family: monospace, Consolas, &quot;Courier New&quot;, monospace; font-weight: normal; font-size: 14px; font-feature-settings: &quot;liga&quot; 0, &quot;calt&quot; 0; font-variation-settings: normal; line-height: 19px; letter-spacing: 0px; top: 0px; left: 6px; width: 76992px; height: 1px;"></textarea><div class="monaco-editor-background textAreaCover" style="position: absolute; top: 0px; left: 0px; width: 0px; height: 0px;"></div><div data-mprt="4" class="overlayWidgets" style="width: 1154px;"></div><div data-mprt="8" class="minimap slider-mouseover" role="presentation" aria-hidden="true" style="position: absolute; left: 0px; width: 0px; height: 884px;"><div class="minimap-shadow-hidden" style="height: 884px;"></div><canvas width="0" height="1326" style="position: absolute; left: 0px; width: 0px; height: 884px;"></canvas><canvas class="minimap-decorations-layer" width="0" height="1326" style="position: absolute; left: 0px; width: 0px; height: 884px;"></canvas><div class="minimap-slider" style="position: absolute; transform: translate3d(0px, 0px, 0px); contain: strict; width: 0px; will-change: unset;"><div class="minimap-slider-horizontal" style="position: absolute; width: 0px; height: 0px;"></div></div></div><div role="presentation" aria-hidden="true" class="blockDecorations-container"></div></div><div data-mprt="2" class="overflowingContentWidgets" style="display: none;"><div widgetid="editor.contrib.resizableContentHoverWidget" style="position: fixed; height: 10px; width: 10px; z-index: 50; display: none; visibility: hidden; max-width: 1280px;"><div class="monaco-sash vertical" style="left: 8px;"></div><div class="monaco-sash vertical" style="left: -2px;"></div><div class="monaco-sash orthogonal-edge-north horizontal" style="top: -2px;"><div class="orthogonal-drag-handle start"></div><div class="orthogonal-drag-handle end"></div></div><div class="monaco-sash orthogonal-edge-south horizontal" style="top: 8px;"><div class="orthogonal-drag-handle start"></div><div class="orthogonal-drag-handle end"></div></div><div class="monaco-hover hidden" tabindex="0" role="tooltip"><div class="monaco-scrollable-element " role="presentation" style="position: relative; overflow: hidden;"><div class="monaco-hover-content" style="overflow: hidden; font-size: 14px; line-height: 1.35714; max-width: 761.64px; max-height: 250px;"></div><div role="presentation" aria-hidden="true" class="invisible scrollbar horizontal" style="position: absolute;"><div class="slider" style="position: absolute; top: 0px; left: 0px; height: 10px; transform: translate3d(0px, 0px, 0px); contain: strict;"></div></div><div role="presentation" aria-hidden="true" class="invisible scrollbar vertical" style="position: absolute;"><div class="slider" style="position: absolute; top: 0px; left: 0px; width: 10px; transform: translate3d(0px, 0px, 0px); contain: strict;"></div></div><div class="shadow"></div><div class="shadow"></div><div class="shadow"></div></div></div></div></div><div class=".in-cell-overflowing"><div widgetid="editor.contrib.quickInputWidget" style="position: absolute; top: 0px; right: 50%;"></div></div></div></div></div><colab-form class="formview vertical layout flex"><div class="widget-area vertical layout"></div></colab-form></div>
    <div class="output" aria-label="Cell 0 output" role="region"><!----> <div class="output-header"> </div>
        <div class="output-content">
          <div class="output-info"><colab-output-info title="Clear output

executed by Nithish
Wednesday, July 3, 2024 (5 days ago)
executed in 10.661s"><template shadowrootmode="open"><!----><md-icon-button title="Code cell output actions" data-aria-label="Code cell output actions" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Code cell output actions">
        <!--?lit$571398431$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$571398431$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$571398431$--><span class="icon"><slot></slot></span>
        <!--?lit$571398431$-->
        <!--?lit$571398431$--><span class="touch"></span>
        <!--?lit$571398431$-->
  </button></template>
        <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$571398431$--><svg viewBox="0 0 24 24"><!--?lit$571398431$--><path d="m15.9 3.07c-4.32 0.0742-8.64-0.0355-13 0.0568-1.37 0.307-1.74 2.1-1.41 3.26 0.469 0.606 1.86 0.384 1.66-0.525 0.0448-0.329-0.183-0.93 0.354-0.766h13.3v1.53h1.71c0.0709-1.13 0.141-2.62-0.968-3.3-0.511-0.264-1.11-0.252-1.67-0.259zm2.94 6.84v4.87c1.62-1.62 3.24-3.24 4.87-4.87h-4.87zm0 0h-1.71v3.43l1.57 1.57c0.32-1.65 0.0556-3.34 0.135-5zm-1.71 3.43v-3.43h-3.43c1.14 1.14 2.29 2.29 3.43 3.43zm1.4 4.27h-1.71v1.48h-13.6v-1.48h-1.71c-0.0473 1.15-0.16 2.72 1.09 3.29 1.47 0.506 3.02 0.0265 4.53 0.192 3.34-0.0051 6.68 0.0336 10-0.0245 1.49-0.366 1.56-2.22 1.42-3.45zm-10.1-1.12c-0.398-0.483-0.796-0.967-1.19-1.45 0.59-0.683 1.18-1.37 1.77-2.05h-8.67v-2h8.67c-0.59-0.683-1.18-1.37-1.77-2.05 0.398-0.483 0.796-0.967 1.19-1.45 1.28 1.5 2.56 3 3.84 4.5-1.28 1.5-2.56 3-3.84 4.5z"></path></svg></md-icon>
      </md-icon-button></template></colab-output-info></div>
          <div class="output-iframe-container">
            <div class="output-iframe-sizer"> <div><div><colab-static-output-renderer tabindex="0" role="group"><div><div class="stream output_text"><pre>Welcome to the Rule-Based Chatbot!
You can start chatting with the bot. Type 'bye' to exit.
You: hi
Bot: Hi there! What can I do for you?
You: bye
Bot: Goodbye!
</pre></div></div><div></div></colab-static-output-renderer></div></div><div><div></div></div></div>
          </div>
        </div></div></div><colab-cell-next-steps><template shadowrootmode="open"><!----></template></colab-cell-next-steps></div></div><div class="add-cell">
      <hr>
    </div></div></div>
              </div>
            </div>
          <div class="sidebar" style="display: none;"></div></div>
          <!--?lit$571398431$--> <div class="footer-links">
      <a target="_blank" href="https://colab.research.google.com/signup?utm_source=footer&amp;utm_medium=link&amp;utm_campaign=footer_links">
        <!--?lit$571398431$-->Colab paid products
      </a>
      -
      <a href="https://colab.research.google.com/cancel-subscription" target="_blank">
        <!--?lit$571398431$-->Cancel contracts here
      </a>
    </div>
        </div>
      </colab-shaded-scroller>
      <div class="notebook-scroll-shadow"></div>
    </div></colab-tab></div>
  </div></colab-tab-pane>
      <colab-resizer style="height: 33.3%" class="sn-resize no-tabs"><div class="resizer-thumb"></div>
        <!--?lit$571398431$--><colab-tab-pane class="layout vertical grow no-tabs" align="horizontal"><!----> <div class="layout vertical grow">
    <div class="tab-pane-header layout horizontal noshrink">
      <md-tabs><template shadowrootmode="open"><!---->
      <div class="tabs">
        <slot></slot>
      </div>
      <md-divider part="divider"><template shadowrootmode="open"><!----></template></md-divider>
    </template></md-tabs>
      <div class="layout grow"></div>
      <!--?lit$571398431$--> <md-icon-button title="Show more" data-aria-label="Show more" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Show more">
        <!--?lit$571398431$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$571398431$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$571398431$--><span class="icon"><slot></slot></span>
        <!--?lit$571398431$-->
        <!--?lit$571398431$--><span class="touch"></span>
        <!--?lit$571398431$-->
  </button></template>
    <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>more_horiz</md-icon>
  </md-icon-button>
    </div>
    <div class="layout vertical grow tab-pane-container"> </div>
  </div></colab-tab-pane>
      </colab-resizer>
    </div>
      <colab-resizer style="width: 37%" class="we-resize no-tabs"><div class="resizer-thumb"></div>
        <!--?lit$571398431$--> <div class="layout vertical tab-pane-parent">
      <!--?lit$571398431$--><colab-tab-pane class="layout vertical grow no-tabs" align="horizontal"><!----> <div class="layout vertical grow">
    <div class="tab-pane-header layout horizontal noshrink">
      <md-tabs><template shadowrootmode="open"><!---->
      <div class="tabs">
        <slot></slot>
      </div>
      <md-divider part="divider"><template shadowrootmode="open"><!----></template></md-divider>
    </template></md-tabs>
      <div class="layout grow"></div>
      <!--?lit$571398431$--> <md-icon-button title="Show more" data-aria-label="Show more" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Show more">
        <!--?lit$571398431$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$571398431$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$571398431$--><span class="icon"><slot></slot></span>
        <!--?lit$571398431$-->
        <!--?lit$571398431$--><span class="touch"></span>
        <!--?lit$571398431$-->
  </button></template>
    <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>more_horiz</md-icon>
  </md-icon-button>
    </div>
    <div class="layout vertical grow tab-pane-container"> </div>
  </div></colab-tab-pane>
      <colab-resizer style="height: 33.3%" class="sn-resize no-tabs"><div class="resizer-thumb"></div>
        <!--?lit$571398431$--><colab-tab-pane class="layout vertical grow no-tabs" align="horizontal"><!----> <div class="layout vertical grow">
    <div class="tab-pane-header layout horizontal noshrink">
      <md-tabs><template shadowrootmode="open"><!---->
      <div class="tabs">
        <slot></slot>
      </div>
      <md-divider part="divider"><template shadowrootmode="open"><!----></template></md-divider>
    </template></md-tabs>
      <div class="layout grow"></div>
      <!--?lit$571398431$--> <md-icon-button title="Show more" data-aria-label="Show more" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Show more">
        <!--?lit$571398431$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$571398431$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$571398431$--><span class="icon"><slot></slot></span>
        <!--?lit$571398431$-->
        <!--?lit$571398431$--><span class="touch"></span>
        <!--?lit$571398431$-->
  </button></template>
    <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>more_horiz</md-icon>
  </md-icon-button>
    </div>
    <div class="layout vertical grow tab-pane-container"> </div>
  </div></colab-tab-pane>
      </colab-resizer>
    </div>
      </colab-resizer>
    </div></colab-tab-layout-container>
        </div>
        <div class="proxies"><div><colab-dom-lifecycle-events style="display: none;"></colab-dom-lifecycle-events><iframe allow="" sandbox="allow-downloads allow-forms allow-pointer-lock allow-popups allow-same-origin allow-scripts allow-storage-access-by-user-activation allow-popups-to-escape-sandbox" src="./Task 1 - Chatbot with Rule-based responses_files/outputframe.html" style="width: 1px; height: 1px; position: absolute; top: -100px;"></iframe></div><div><colab-dom-lifecycle-events style="display: none;"></colab-dom-lifecycle-events><iframe allow="accelerometer; autoplay; gyroscope; magnetometer; xr-spatial-tracking; clipboard-write; camera; microphone; serial; usb" sandbox="allow-downloads allow-forms allow-pointer-lock allow-popups allow-same-origin allow-scripts allow-storage-access-by-user-activation allow-modals allow-popups-to-escape-sandbox" src="./Task 1 - Chatbot with Rule-based responses_files/outputframe(1).html" style="width: 1px; height: 1px; position: absolute; top: -100px;"></iframe></div></div>
      <colab-file-viewer-manager></colab-file-viewer-manager></div>
    <colab-status-bar role="region" aria-label="Runtime status bar" style="min-height: inherit;"><template shadowrootmode="open"><!----> <!--?lit$571398431$--><div class="frames"></div>
      <md-icon-button class="visible-on-closed" title="Runtime disconnected" data-aria-label="Runtime disconnected" disabled="" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Runtime disconnected" disabled="">
        <!--?lit$571398431$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$571398431$--><md-ripple disabled="" aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$571398431$--><span class="icon"><slot></slot></span>
        <!--?lit$571398431$-->
        <!--?lit$571398431$--><span class="touch"></span>
        <!--?lit$571398431$-->
  </button></template>
        <md-icon filled="" class="visible-on-closed" status="" aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$571398431$-->fiber_manual_record</md-icon>
      </md-icon-button>
      <md-icon-button title="Close" data-aria-label="Close" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Close">
        <!--?lit$571398431$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$571398431$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$571398431$--><span class="icon"><slot></slot></span>
        <!--?lit$571398431$-->
        <!--?lit$571398431$--><span class="touch"></span>
        <!--?lit$571398431$-->
  </button></template>
        <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>close</md-icon>
      </md-icon-button></template></colab-status-bar></div><div class="goog-menu colab-styled-scroller" id="file-menu" role="menu" aria-haspopup="true" aria-activedescendant="download-submenu-menu-button" style="user-select: none; max-height: 532px; visibility: visible; left: 64px; top: 61px; display: none;"><!--?lit$571398431$--><div command="locate-in-drive" class="goog-menuitem" role="menuitem" id=":2" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$571398431$-->Locate in Drive<!--?lit$571398431$--></div></div><div command="open-in-playground" class="goog-menuitem" role="menuitem" id=":3" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$571398431$-->Open in playground mode<!--?lit$571398431$--></div></div><div class="goog-menuseparator goog-menuitem-disabled" aria-disabled="true" role="separator" id=":4" style="user-select: none;"></div><div command="new" class="goog-menuitem" role="menuitem" id=":5" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$571398431$-->New notebook in Drive<!--?lit$571398431$--></div></div><div command="open" class="goog-menuitem" role="menuitem" id=":6" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$571398431$-->Open notebook<!--?lit$571398431$--><span class="goog-menuitem-accel">Ctrl+O</span></div></div><div command="import-notebook" class="goog-menuitem" role="menuitem" id=":7" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$571398431$-->Upload notebook<!--?lit$571398431$--></div></div><div class="goog-menuseparator goog-menuitem-disabled" aria-disabled="true" role="separator" id=":8" style="user-select: none;"></div><div command="rename" class="goog-menuitem" role="menuitem" id=":9" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$571398431$-->Rename<!--?lit$571398431$--></div></div><div command="move-notebook" class="goog-menuitem" role="menuitem" id=":a" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$571398431$-->Move<!--?lit$571398431$--></div></div><div command="trash" class="goog-menuitem" role="menuitem" id=":b" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$571398431$-->Move to trash<!--?lit$571398431$--></div></div><div class="goog-menuseparator goog-menuitem-disabled" aria-disabled="true" role="separator" id=":c" style="user-select: none;"></div><div command="clone" class="goog-menuitem" role="menuitem" id=":d" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$571398431$-->Save a copy in Drive<!--?lit$571398431$--></div></div><div command="copy-to-gist" class="goog-menuitem" role="menuitem" id=":e" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$571398431$-->Save a copy as a GitHub Gist<!--?lit$571398431$--></div></div><div command="copy-to-github" class="goog-menuitem" role="menuitem" id=":f" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$571398431$-->Save a copy in GitHub<!--?lit$571398431$--></div></div><div class="goog-menuseparator goog-menuitem-disabled" aria-disabled="true" role="separator" id=":g" style="user-select: none;"></div><div command="save" class="goog-menuitem" role="menuitem" id=":h" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$571398431$-->Save<!--?lit$571398431$--><span class="goog-menuitem-accel">Ctrl+S</span></div></div><div command="save-and-checkpoint" class="goog-menuitem" role="menuitem" id=":i" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$571398431$-->Save and pin revision<!--?lit$571398431$--><span class="goog-menuitem-accel">Ctrl+M S</span></div></div><div command="show-history" class="goog-menuitem" role="menuitem" id=":j" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$571398431$-->Revision history<!--?lit$571398431$--></div></div><div class="goog-menuseparator goog-menuitem-disabled" aria-disabled="true" role="separator" id=":k" style="user-select: none;"></div><div class="goog-submenu goog-menuitem goog-menuitem-highlight" id="download-submenu-menu-button" role="menuitem" aria-haspopup="true" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;">
      <!--?lit$571398431$-->Download
    <span class="goog-submenu-arrow" style="user-select: none;">►</span></div></div><div command="print" class="goog-menuitem" role="menuitem" id=":o" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$571398431$-->Print<!--?lit$571398431$--><span class="goog-menuitem-accel">Ctrl+P</span></div></div></div><div class="goog-menu" id="download-submenu-menu" role="menu" aria-haspopup="true" style="user-select: none; left: 375.667px; top: 513.667px; display: none;"><!--?lit$571398431$--><div command="download-ipynb" class="goog-menuitem" role="menuitem" id=":m" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$571398431$-->Download .ipynb<!--?lit$571398431$--></div></div><div command="download-python" class="goog-menuitem" role="menuitem" id=":n" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$571398431$-->Download .py<!--?lit$571398431$--></div></div></div><div class="goog-menu colab-styled-scroller" id="edit-menu" role="menu" aria-haspopup="true" style="user-select: none; max-height: 532px; visibility: visible; left: 99.2917px; top: 61px; display: none;"><!--?lit$571398431$--><div command="undo" class="goog-menuitem goog-menuitem-disabled" role="menuitem" id=":q" aria-disabled="true" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;">Undo<span class="goog-menuitem-accel">Ctrl+M Z</span></div></div><div command="redo" class="goog-menuitem goog-menuitem-disabled" role="menuitem" id=":r" aria-disabled="true" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;">Redo<span class="goog-menuitem-accel">Ctrl+Shift+Y</span></div></div><div class="goog-menuseparator goog-menuitem-disabled" aria-disabled="true" role="separator" id=":s" style="user-select: none;"></div><div command="select-all" class="goog-menuitem" role="menuitem" id=":t" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$571398431$-->Select all cells<!--?lit$571398431$--><span class="goog-menuitem-accel">Ctrl+Shift+A</span></div></div><div command="cut" class="goog-menuitem" role="menuitem" id=":u" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$571398431$-->Cut cell or selection<!--?lit$571398431$--></div></div><div command="copy" class="goog-menuitem" role="menuitem" id=":v" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$571398431$-->Copy cell or selection<!--?lit$571398431$--></div></div><div command="paste" class="goog-menuitem" role="menuitem" id=":w" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$571398431$-->Paste<!--?lit$571398431$--></div></div><div command="delete-cell-or-selection" class="goog-menuitem" role="menuitem" id=":x" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$571398431$-->Delete selected cells<!--?lit$571398431$--><span class="goog-menuitem-accel">Ctrl+M D</span></div></div><div class="goog-menuseparator goog-menuitem-disabled" aria-disabled="true" role="separator" id=":y" style="user-select: none;"></div><div command="find" class="goog-menuitem " role="menuitem" id=":z" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$571398431$-->Find and replace<!--?lit$571398431$--><span class="goog-menuitem-accel">Ctrl+H</span></div></div><div command="find-next" class="goog-menuitem " role="menuitem" id=":10" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$571398431$-->Find next<!--?lit$571398431$--><span class="goog-menuitem-accel">Ctrl+G</span></div></div><div command="find-previous" class="goog-menuitem " role="menuitem" id=":11" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$571398431$-->Find previous<!--?lit$571398431$--><span class="goog-menuitem-accel">Ctrl+Shift+G</span></div></div><div class="goog-menuseparator goog-menuitem-disabled" aria-disabled="true" role="separator" id=":12" style="user-select: none;"></div><div command="notebook-settings" class="goog-menuitem " role="menuitem" id=":13" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$571398431$-->Notebook settings<!--?lit$571398431$--></div></div><div class="goog-menuseparator goog-menuitem-disabled" aria-disabled="true" role="separator" id=":14" style="user-select: none;"></div><div command="clear-outputs" class="goog-menuitem " role="menuitem" id=":15" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$571398431$-->Clear all outputs<!--?lit$571398431$--></div></div></div><div class="goog-menu" id="view-menu" role="menu" aria-haspopup="true" style="display: none; user-select: none;"><!--?lit$571398431$--><div command="show-toc-pane" class="goog-menuitem goog-option" role="menuitemcheckbox" aria-checked="false" id=":17" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><div class="goog-menuitem-checkbox" style="user-select: none;"><!----><md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>check</md-icon> </div><!--?lit$571398431$-->Table of contents<!--?lit$571398431$--></div></div><div command="show-fileinfo" class="goog-menuitem " role="menuitem" id=":18" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$571398431$-->Notebook info<!--?lit$571398431$--></div></div><div command="show-executedcode" class="goog-menuitem " role="menuitem" id=":19" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$571398431$-->Executed code history<!--?lit$571398431$--></div></div><div command="toggle-comments-visibility" class="goog-menuitem goog-option" role="menuitemcheckbox" aria-checked="false" id=":1a" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><div class="goog-menuitem-checkbox" style="user-select: none;"><!----><md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>check</md-icon> </div><!--?lit$571398431$-->Comments sidebar<!--?lit$571398431$--></div></div><div class="goog-menuseparator goog-menuitem-disabled" aria-disabled="true" role="separator" id=":1b" style="user-select: none;"></div><div command="collapse-sections" class="goog-menuitem " role="menuitem" id=":1c" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$571398431$-->Collapse sections<!--?lit$571398431$--></div></div><div command="expand-sections" class="goog-menuitem " role="menuitem" id=":1d" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$571398431$-->Expand sections<!--?lit$571398431$--></div></div><div command="save-section-layout" class="goog-menuitem " role="menuitem" id=":1e" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$571398431$-->Save collapsed section layout<!--?lit$571398431$--></div></div><div class="goog-menuseparator goog-menuitem-disabled" aria-disabled="true" role="separator" id=":1f" style="user-select: none;"></div><div command="hide-code" class="goog-menuitem " role="menuitem" id=":1g" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$571398431$-->Show/hide code<!--?lit$571398431$--></div></div><div command="toggle-output" class="goog-menuitem " role="menuitem" id=":1h" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$571398431$-->Show/hide output<!--?lit$571398431$--></div></div><div class="goog-menuseparator goog-menuitem-disabled" aria-disabled="true" role="separator" id=":1i" style="user-select: none;"></div><div command="focus-next-tab" class="goog-menuitem " role="menuitem" id=":1j" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$571398431$-->Focus next tab<!--?lit$571398431$--></div></div><div command="focus-previous-tab" class="goog-menuitem " role="menuitem" id=":1k" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$571398431$-->Focus previous tab<!--?lit$571398431$--></div></div><div command="move-tab-to-next" class="goog-menuitem " role="menuitem" id=":1l" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$571398431$-->Move tab to next pane<!--?lit$571398431$--></div></div><div command="move-tab-to-prev" class="goog-menuitem " role="menuitem" id=":1m" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$571398431$-->Move tab to previous pane<!--?lit$571398431$--></div></div></div><div class="goog-menu" id="insert-menu" role="menu" aria-haspopup="true" style="display: none; user-select: none;"><!--?lit$571398431$--><div command="insert-cell-below" class="goog-menuitem " role="menuitem" id=":1o" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$571398431$-->Code cell<!--?lit$571398431$--></div></div><div command="add-text" class="goog-menuitem " role="menuitem" id=":1p" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$571398431$-->Text cell<!--?lit$571398431$--></div></div><div command="add-section-header" class="goog-menuitem " role="menuitem" id=":1q" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$571398431$-->Section header cell<!--?lit$571398431$--></div></div><div class="goog-menuseparator goog-menuitem-disabled" aria-disabled="true" role="separator" id=":1r" style="user-select: none;"></div><div command="open-scratch-code-cell" class="goog-menuitem " role="menuitem" id=":1s" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$571398431$-->Scratch code cell<!--?lit$571398431$--></div></div><div command="snippets" class="goog-menuitem " role="menuitem" id=":1t" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$571398431$-->Code snippets<!--?lit$571398431$--></div></div><div class="goog-menuseparator goog-menuitem-disabled" aria-disabled="true" role="separator" id=":1u" style="user-select: none;"></div><div command="add-form-field" class="goog-menuitem " role="menuitem" id=":1v" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$571398431$-->Add a form field<!--?lit$571398431$--></div></div></div><div class="goog-menu" id="runtime-menu" role="menu" aria-haspopup="true" style="display: none; user-select: none;"><!--?lit$571398431$--><div command="runall" class="goog-menuitem " role="menuitem" id=":1x" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$571398431$-->Run all<!--?lit$571398431$--></div></div><div command="runbefore" class="goog-menuitem " role="menuitem" id=":1y" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$571398431$-->Run before<!--?lit$571398431$--></div></div><div command="runfocused" class="goog-menuitem " role="menuitem" id=":1z" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$571398431$-->Run the focused cell<!--?lit$571398431$--></div></div><div command="runselected" class="goog-menuitem " role="menuitem" id=":20" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$571398431$-->Run selection<!--?lit$571398431$--></div></div><div command="runafter" class="goog-menuitem " role="menuitem" id=":21" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$571398431$-->Run after<!--?lit$571398431$--></div></div><div class="goog-menuseparator goog-menuitem-disabled" aria-disabled="true" role="separator" id=":22" style="user-select: none;"></div><div command="interrupt" class="goog-menuitem " role="menuitem" id=":23" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$571398431$-->Interrupt execution<!--?lit$571398431$--></div></div><div command="restart" class="goog-menuitem " role="menuitem" id=":24" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$571398431$-->Restart session<!--?lit$571398431$--></div></div><div command="restart-and-run-all" class="goog-menuitem " role="menuitem" id=":25" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$571398431$-->Restart session and run all<!--?lit$571398431$--></div></div><div command="powerwash-current-vm" class="goog-menuitem " role="menuitem" id=":26" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$571398431$-->Disconnect and delete runtime<!--?lit$571398431$--></div></div><div class="goog-menuseparator goog-menuitem-disabled" aria-disabled="true" role="separator" id=":27" style="user-select: none;"></div><div command="change-runtime-type" class="goog-menuitem " role="menuitem" id=":28" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$571398431$-->Change runtime type<!--?lit$571398431$--></div></div><div class="goog-menuseparator goog-menuitem-disabled" aria-disabled="true" role="separator" id=":29" style="user-select: none;"></div><div command="manage-sessions" class="goog-menuitem " role="menuitem" id=":2a" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$571398431$-->Manage sessions<!--?lit$571398431$--></div></div><div command="open-resource-viewer" class="goog-menuitem " role="menuitem" id=":2b" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$571398431$-->View resources<!--?lit$571398431$--></div></div><div command="view-runtime-logs" class="goog-menuitem " role="menuitem" id=":2c" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$571398431$-->View runtime logs<!--?lit$571398431$--></div></div></div><div class="goog-menu" id="tools-menu" role="menu" aria-haspopup="true" style="display: none; user-select: none;"><!--?lit$571398431$--><div command="show-command-palette" class="goog-menuitem " role="menuitem" id=":2e" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$571398431$-->Command palette<!--?lit$571398431$--></div></div><div class="goog-menuseparator goog-menuitem-disabled" aria-disabled="true" role="separator" id=":2f" style="user-select: none;"></div><div command="preferences" class="goog-menuitem " role="menuitem" id=":2g" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$571398431$-->Settings<!--?lit$571398431$--></div></div><div command="shortcuts" class="goog-menuitem " role="menuitem" id=":2h" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$571398431$-->Keyboard shortcuts<!--?lit$571398431$--></div></div><div class="goog-menuseparator goog-menuitem-disabled" aria-disabled="true" role="separator" id=":2i" style="user-select: none;"></div><div command="open-differ" class="goog-menuitem " role="menuitem" id=":2j" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$571398431$-->Diff notebooks<!--?lit$571398431$--> <span class="screenreader-only" style="user-select: none;"><!--?lit$571398431$-->(opens in a new tab)</span></div></div></div><div class="goog-menu" id="help-menu" role="menu" aria-haspopup="true" style="display: none; user-select: none;"><!--?lit$571398431$--><div command="faq" class="goog-menuitem " role="menuitem" id=":2l" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$571398431$-->Frequently asked questions<!--?lit$571398431$--></div></div><div command="view-relnotes" class="goog-menuitem " role="menuitem" id=":2m" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$571398431$-->View release notes<!--?lit$571398431$--></div></div><div command="snippets" class="goog-menuitem " role="menuitem" id=":2n" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$571398431$-->Search code snippets<!--?lit$571398431$--></div></div><div class="goog-menuseparator goog-menuitem-disabled" aria-disabled="true" role="separator" id=":2o" style="user-select: none;"></div><div command="report-bug" class="goog-menuitem " role="menuitem" id=":2p" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$571398431$-->Report a bug<!--?lit$571398431$--></div></div><div command="report-abuse" class="goog-menuitem " role="menuitem" id=":2q" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$571398431$-->Report Drive abuse<!--?lit$571398431$--></div></div><div command="send-feedback" class="goog-menuitem " role="menuitem" id=":2r" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$571398431$-->Send feedback<!--?lit$571398431$--></div></div><div command="view-tos" class="goog-menuitem " role="menuitem" id=":2s" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$571398431$-->View terms of service<!--?lit$571398431$--></div></div></div><div class="doc-comments-area" style="display: none;"><!----><div class="doc-comments-buttons">
        <md-text-button command="add-comment" value="" has-icon=""><template shadowrootmode="open" shadowrootdelegatesfocus><!---->
      <!--?lit$571398431$-->
      <div class="background"></div>
      <md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
      <md-ripple part="ripple" for="button" aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
      <!--?lit$571398431$--><button id="button" class="button">
      <!--?lit$571398431$-->
      <span class="touch"></span>
      <!--?lit$571398431$--><slot name="icon"></slot>
      <span class="label"><slot></slot></span>
      <!--?lit$571398431$-->
    
    </button>
    </template>
          <md-icon slot="icon" filled="" aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>comment</md-icon>
          <!--?lit$571398431$-->Add a comment
        </md-text-button>
      </div></div><div class="thumbnail"></div><div class="monaco-aria-container"><div class="monaco-alert" role="alert" aria-atomic="true"></div><div class="monaco-alert" role="alert" aria-atomic="true"></div><div class="monaco-status" role="complementary" aria-live="polite" aria-atomic="true"></div><div class="monaco-status" role="complementary" aria-live="polite" aria-atomic="true"></div></div><iframe id="apiproxy2123e87de58199fb20266c3f7383ac4825b4486c0.396873913" name="apiproxy2123e87de58199fb20266c3f7383ac4825b4486c0.396873913" src="./Task 1 - Chatbot with Rule-based responses_files/proxy.html" tabindex="-1" aria-hidden="true" style="width: 1px; height: 1px; position: absolute; top: -100px; display: none;"></iframe><span id="PING_IFRAME_FORM_DETECTION" style="display: none;"></span><iframe src="./Task 1 - Chatbot with Rule-based responses_files/bscframe.html" style="display: none;"></iframe><div><div class="grecaptcha-badge" data-style="bottomright" style="width: 256px; height: 60px; position: fixed; visibility: hidden; display: block; transition: right 0.3s ease 0s; bottom: 14px; right: -186px; box-shadow: gray 0px 0px 5px; border-radius: 2px; overflow: hidden;"><div class="grecaptcha-logo"><iframe title="reCAPTCHA" width="256" height="60" role="presentation" name="a-90jnvrr41ykj" frameborder="0" scrolling="no" sandbox="allow-forms allow-popups allow-same-origin allow-scripts allow-top-navigation allow-modals allow-popups-to-escape-sandbox allow-storage-access-by-user-activation" src="./Task 1 - Chatbot with Rule-based responses_files/anchor.html"></iframe></div><div class="grecaptcha-error"></div><textarea id="g-recaptcha-response-100000" name="g-recaptcha-response" class="g-recaptcha-response" style="width: 250px; height: 40px; border: 1px solid rgb(193, 193, 193); margin: 10px 25px; padding: 0px; resize: none; display: none;"></textarea></div><iframe style="display: none;" src="./Task 1 - Chatbot with Rule-based responses_files/saved_resource.html"></iframe></div><iframe id="hfcr" src="./Task 1 - Chatbot with Rule-based responses_files/RotateCookiesPage.html" style="display: none;"></iframe><span id="PING_CONTENT_DLS_POPUP" style="display: none;"></span><div style="background-color: transparent; border: none; bottom: 15px; display: block; margin: 0px; opacity: 1; padding: 0px; position: fixed; right: 15px; z-index: 2147483646;"><template shadowrootmode="closed"><style>/*!
 * 
 *     MCAFEE RESTRICTED CONFIDENTIAL
 *     Copyright (c) 2024 McAfee, LLC
 *
 *     The source code contained or described herein and all documents related
 *     to the source code ("Material") are owned by McAfee or its
 *     suppliers or licensors. Title to the Material remains with McAfee
 *     or its suppliers and licensors. The Material contains trade
 *     secrets and proprietary and confidential information of McAfee or its
 *     suppliers and licensors. The Material is protected by worldwide copyright
 *     and trade secret laws and treaty provisions. No part of the Material may
 *     be used, copied, reproduced, modified, published, uploaded, posted,
 *     transmitted, distributed, or disclosed in any way without McAfee's prior
 *     express written permission.
 *
 *     No license under any patent, copyright, trade secret or other intellectual
 *     property right is granted to or conferred upon you by disclosure or
 *     delivery of the Materials, either expressly, by implication, inducement,
 *     estoppel or otherwise. Any license under such intellectual property rights
 *     must be expressed and approved by McAfee in writing.
 *
 */
@import url(https://fonts.googleapis.com/css2?family=Open+Sans:ital,wght@0,300;0,400;0,500;0,600;0,700;0,800;1,300;1,400;1,500;1,600;1,700;1,800&family=Poppins:ital,wght@0,400;0,500;0,600;0,800;1,400;1,500;1,600;1,800&display=swap);
*{border:0;box-sizing:border-box;font:inherit;font-family:"mcafeeOpenSans","Open Sans",Arial,Helvetica,sans-serif;font-size:100%;margin:0;padding:0;vertical-align:baseline;outline:none}article,aside,details,figcaption,figure,footer,header,hgroup,menu,nav,section{display:block}html,body{background-color:#f5f6fa;font-family:"Open Sans","mcafeeOpenSans",Arial,Helvetica,sans-serif;line-height:1;height:100%;width:100%}ol,ul{list-style:none}blockquote,q{quotes:none}blockquote:after,blockquote:before,q:after,q:before{content:"";content:none}table{border-collapse:collapse;border-spacing:0}b{font-weight:bold}img{display:block}.dls__container{align-items:center;display:flex;margin:0 auto;margin-top:50px;position:relative}.dls__popup__expanded{align-items:center;overflow:hidden;border-radius:100px;cursor:pointer;display:flex;left:0;padding:15px;position:absolute;height:95px;width:383px;background-color:#fff;transition:all .3s ease-in-out}.dls__popup__expanded .dls__icon{height:65px;width:73px}.content{margin-left:12px}.content .content__images{display:flex;align-items:center;width:250px}.content .content__images .seperator__line{margin-left:5px;margin-right:10px}.content .content__images #dls_close_icon{cursor:pointer;margin-left:auto;margin-right:0px}.content p{font-family:"Poppins",Arial,Helvetica,sans-serif;font-weight:"400";font-size:14px;line-height:20px;margin-top:8px;color:#4258ff;width:250px;cursor:pointer}.shield{overflow:hidden;box-shadow:0px 2px 4px 0px rgba(33,41,52,.12),0px -1px 2px 0px rgba(0,0,0,.08);align-items:center;border-radius:100px;bottom:0;display:flex;height:95px;justify-content:center;position:absolute;right:0;width:383px;transition:all .3s ease-in-out}.shield__circle{display:flex;justify-content:center;align-items:center;width:55px;height:55px;background-color:#c01818;transition:all .6s ease-in-out .2s;z-index:1;opacity:0}

/*# sourceMappingURL=../sourceMap/chrome/css/download_scan_popup.css.map*/</style><div class="dls__container">
  <div class="shield" style="background: transparent; opacity: 0.1; display: none;">
    <div class="shield__circle" style="opacity: 1;">
      <img src="chrome-extension://fheoggkfdfchfphceeifdbepaooicaho/images/download_scan/mcafee_logo_white.svg?secret=kxbzar" x-mcsrc="" id="dls_ballon_icon" x-mcsrcparsed="true">
    </div>
    <div class="dls__popup__expanded" style="opacity: 0;">
      <img src="chrome-extension://fheoggkfdfchfphceeifdbepaooicaho/images/download_scan/download_scan_icon.svg?secret=kxbzar" x-mcsrc="" class="dls__icon" x-mcsrcparsed="true">
      <div class="content">
        <div class="content__images">
          <img src="chrome-extension://fheoggkfdfchfphceeifdbepaooicaho/images/download_scan/mcafee_logo_red.svg?secret=kxbzar" x-mcsrc="" id="dls_mcafee_logo" x-mcsrcparsed="true">
          <img src="chrome-extension://fheoggkfdfchfphceeifdbepaooicaho/images/download_scan/seperator_line.svg?secret=kxbzar" x-mcsrc="" class="seperator__line" x-mcsrcparsed="true">
          <img src="chrome-extension://fheoggkfdfchfphceeifdbepaooicaho/images/download_scan/webadvisor.svg?secret=kxbzar" x-mcsrc="" x-mcsrcparsed="true">
          <img src="chrome-extension://fheoggkfdfchfphceeifdbepaooicaho/images/download_scan/close-outline.svg?secret=kxbzar" x-mcsrc="" id="dls_close_icon" x-mcsrcparsed="true">
        </div>
        <p id="download_scan_popup_expanded_descriptions">Your download's being scanned. We'll let you know if there's an issue.</p>
      </div>
    </div>
  </div>
</div><style>/*!
 * 
 *     MCAFEE RESTRICTED CONFIDENTIAL
 *     Copyright (c) 2024 McAfee, LLC
 *
 *     The source code contained or described herein and all documents related
 *     to the source code ("Material") are owned by McAfee or its
 *     suppliers or licensors. Title to the Material remains with McAfee
 *     or its suppliers and licensors. The Material contains trade
 *     secrets and proprietary and confidential information of McAfee or its
 *     suppliers and licensors. The Material is protected by worldwide copyright
 *     and trade secret laws and treaty provisions. No part of the Material may
 *     be used, copied, reproduced, modified, published, uploaded, posted,
 *     transmitted, distributed, or disclosed in any way without McAfee's prior
 *     express written permission.
 *
 *     No license under any patent, copyright, trade secret or other intellectual
 *     property right is granted to or conferred upon you by disclosure or
 *     delivery of the Materials, either expressly, by implication, inducement,
 *     estoppel or otherwise. Any license under such intellectual property rights
 *     must be expressed and approved by McAfee in writing.
 *
 */
.mc-interactive-balloon{position:absolute;right:-50px;bottom:8px;box-shadow:rgba(0,0,0,.12) 0px 0px 10px;height:40px;width:40px;background:#1671ee;border-radius:20px;display:flex;justify-content:center;align-items:center}

/*# sourceMappingURL=../sourceMap/chrome/css/interactive_balloon.css.map*/</style></template></div></body></html>