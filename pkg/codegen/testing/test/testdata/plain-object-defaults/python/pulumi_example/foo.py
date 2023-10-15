# coding=utf-8
# *** WARNING: this file was generated by test. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Callable, Mapping, Optional, Sequence, Union, overload
from . import _utilities
from . import outputs
from ._inputs import *

__all__ = ['FooArgs', 'Foo']

@pulumi.input_type
class FooArgs:
    def __init__(__self__, *,
                 backup_kube_client_settings: pulumi.Input['KubeClientSettingsArgs'],
                 argument: Optional[str] = None,
                 kube_client_settings: Optional[pulumi.Input['KubeClientSettingsArgs']] = None,
                 settings: Optional[pulumi.Input['LayeredTypeArgs']] = None):
        """
        The set of arguments for constructing a Foo resource.
        :param pulumi.Input['KubeClientSettingsArgs'] backup_kube_client_settings: Options for tuning the Kubernetes client used by a Provider.
        :param pulumi.Input['KubeClientSettingsArgs'] kube_client_settings: Options for tuning the Kubernetes client used by a Provider.
        :param pulumi.Input['LayeredTypeArgs'] settings: describing things
        """
        FooArgs._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            backup_kube_client_settings=backup_kube_client_settings,
            argument=argument,
            kube_client_settings=kube_client_settings,
            settings=settings,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             backup_kube_client_settings: pulumi.Input['KubeClientSettingsArgs'],
             argument: Optional[str] = None,
             kube_client_settings: Optional[pulumi.Input['KubeClientSettingsArgs']] = None,
             settings: Optional[pulumi.Input['LayeredTypeArgs']] = None,
             opts: Optional[pulumi.ResourceOptions]=None,
             **kwargs):
        if 'backupKubeClientSettings' in kwargs:
            backup_kube_client_settings = kwargs['backupKubeClientSettings']
        if 'kubeClientSettings' in kwargs:
            kube_client_settings = kwargs['kubeClientSettings']

        _setter("backup_kube_client_settings", backup_kube_client_settings)
        if argument is not None:
            _setter("argument", argument)
        if kube_client_settings is not None:
            _setter("kube_client_settings", kube_client_settings)
        if settings is not None:
            _setter("settings", settings)

    @property
    @pulumi.getter(name="backupKubeClientSettings")
    def backup_kube_client_settings(self) -> pulumi.Input['KubeClientSettingsArgs']:
        """
        Options for tuning the Kubernetes client used by a Provider.
        """
        return pulumi.get(self, "backup_kube_client_settings")

    @backup_kube_client_settings.setter
    def backup_kube_client_settings(self, value: pulumi.Input['KubeClientSettingsArgs']):
        pulumi.set(self, "backup_kube_client_settings", value)

    @property
    @pulumi.getter
    def argument(self) -> Optional[str]:
        return pulumi.get(self, "argument")

    @argument.setter
    def argument(self, value: Optional[str]):
        pulumi.set(self, "argument", value)

    @property
    @pulumi.getter(name="kubeClientSettings")
    def kube_client_settings(self) -> Optional[pulumi.Input['KubeClientSettingsArgs']]:
        """
        Options for tuning the Kubernetes client used by a Provider.
        """
        return pulumi.get(self, "kube_client_settings")

    @kube_client_settings.setter
    def kube_client_settings(self, value: Optional[pulumi.Input['KubeClientSettingsArgs']]):
        pulumi.set(self, "kube_client_settings", value)

    @property
    @pulumi.getter
    def settings(self) -> Optional[pulumi.Input['LayeredTypeArgs']]:
        """
        describing things
        """
        return pulumi.get(self, "settings")

    @settings.setter
    def settings(self, value: Optional[pulumi.Input['LayeredTypeArgs']]):
        pulumi.set(self, "settings", value)


class Foo(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 argument: Optional[str] = None,
                 backup_kube_client_settings: Optional[pulumi.Input[pulumi.InputType['KubeClientSettingsArgs']]] = None,
                 kube_client_settings: Optional[pulumi.Input[pulumi.InputType['KubeClientSettingsArgs']]] = None,
                 settings: Optional[pulumi.Input[pulumi.InputType['LayeredTypeArgs']]] = None,
                 __props__=None):
        """
        test new feature with resoruces

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[pulumi.InputType['KubeClientSettingsArgs']] backup_kube_client_settings: Options for tuning the Kubernetes client used by a Provider.
        :param pulumi.Input[pulumi.InputType['KubeClientSettingsArgs']] kube_client_settings: Options for tuning the Kubernetes client used by a Provider.
        :param pulumi.Input[pulumi.InputType['LayeredTypeArgs']] settings: describing things
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: FooArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        test new feature with resoruces

        :param str resource_name: The name of the resource.
        :param FooArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(FooArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            kwargs = kwargs or {}
            def _setter(key, value):
                kwargs[key] = value
            FooArgs._configure(_setter, **kwargs)
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 argument: Optional[str] = None,
                 backup_kube_client_settings: Optional[pulumi.Input[pulumi.InputType['KubeClientSettingsArgs']]] = None,
                 kube_client_settings: Optional[pulumi.Input[pulumi.InputType['KubeClientSettingsArgs']]] = None,
                 settings: Optional[pulumi.Input[pulumi.InputType['LayeredTypeArgs']]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = FooArgs.__new__(FooArgs)

            __props__.__dict__["argument"] = argument
            if backup_kube_client_settings is not None and not isinstance(backup_kube_client_settings, KubeClientSettingsArgs):
                backup_kube_client_settings = backup_kube_client_settings or {}
                def _setter(key, value):
                    backup_kube_client_settings[key] = value
                KubeClientSettingsArgs._configure(_setter, **backup_kube_client_settings)
            if backup_kube_client_settings is None and not opts.urn:
                raise TypeError("Missing required property 'backup_kube_client_settings'")
            __props__.__dict__["backup_kube_client_settings"] = backup_kube_client_settings
            if kube_client_settings is not None and not isinstance(kube_client_settings, KubeClientSettingsArgs):
                kube_client_settings = kube_client_settings or {}
                def _setter(key, value):
                    kube_client_settings[key] = value
                KubeClientSettingsArgs._configure(_setter, **kube_client_settings)
            __props__.__dict__["kube_client_settings"] = kube_client_settings
            if settings is not None and not isinstance(settings, LayeredTypeArgs):
                settings = settings or {}
                def _setter(key, value):
                    settings[key] = value
                LayeredTypeArgs._configure(_setter, **settings)
            __props__.__dict__["settings"] = settings
            __props__.__dict__["default_kube_client_settings"] = None
        super(Foo, __self__).__init__(
            'example:index:Foo',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'Foo':
        """
        Get an existing Foo resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = FooArgs.__new__(FooArgs)

        __props__.__dict__["default_kube_client_settings"] = None
        return Foo(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="defaultKubeClientSettings")
    def default_kube_client_settings(self) -> pulumi.Output[Optional['outputs.KubeClientSettings']]:
        """
        A test for plain types
        """
        return pulumi.get(self, "default_kube_client_settings")

