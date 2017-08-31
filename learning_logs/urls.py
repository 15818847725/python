#定义learning_logs的url模式
from django.conf.urls import url

from . import views

urlpatterns = [
	#主页
	url(r'^$',views.index,name = 'index'),
	#显示所有主题
	url(r'^topics/$',views.topics,name = 'topics'),
	#显示对应的主题内容
	url(r'^topics/(?P<topic_id>\d+)/$',views.topic,name = 'topic'),
	#显示新的主题表单
	url(r'^new_topic/$',views.new_topic,name = 'new_topic'),
	#显示新的对应的主题内容
	url(r'^new_entry/(?P<topic_id>\d+)/$',views.new_entry,name = 'new_entry'),
	#修改对应的主题内容
	url(r'^edit_entry/(?P<entry_id>\d+)/$',views.edit_entry,name = 'edit_entry'),
]
