from south.modelsinspector import add_introspection_rules


add_introspection_rules([], ["^form_designer\.pickled_object_field\.PickledObjectField"])

add_introspection_rules([], ["^form_designer\.template_field\.TemplateFormField"])
add_introspection_rules([], ["^form_designer\.template_field\.TemplateCharField"])
add_introspection_rules([], ["^form_designer\.template_field\.TemplateTextField"])

add_introspection_rules([], ["^form_designer\.model_name_field\.ModelNameFormField"])
add_introspection_rules([], ["^form_designer\.model_name_field\.ModelNameField"])

