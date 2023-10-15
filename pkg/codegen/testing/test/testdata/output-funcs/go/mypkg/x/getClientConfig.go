// Code generated by test DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package mypkg

import (
	"context"
	"reflect"

	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumix"
	"output-funcs/mypkg/internal"
)

// Failing example taken from azure-native. Original doc: Use this function to access the current configuration of the native Azure provider.
func GetClientConfig(ctx *pulumi.Context, opts ...pulumi.InvokeOption) (*GetClientConfigResult, error) {
	opts = internal.PkgInvokeDefaultOpts(opts)
	var rv GetClientConfigResult
	err := ctx.Invoke("mypkg::getClientConfig", nil, &rv, opts...)
	if err != nil {
		return nil, err
	}
	return &rv, nil
}

// Configuration values returned by getClientConfig.
type GetClientConfigResult struct {
	// Azure Client ID (Application Object ID).
	ClientId string `pulumi:"clientId"`
	// Azure Object ID of the current user or service principal.
	ObjectId string `pulumi:"objectId"`
	// Azure Subscription ID
	SubscriptionId string `pulumi:"subscriptionId"`
	// Azure Tenant ID
	TenantId string `pulumi:"tenantId"`
}

func GetClientConfigOutput(ctx *pulumi.Context, opts ...pulumi.InvokeOption) GetClientConfigResultOutput {
	outputResult := pulumix.ApplyErr[int](pulumix.Val(0), func(_ int) (*GetClientConfigResult, error) {
		return GetClientConfig(ctx, opts...)
	})

	return pulumix.Cast[GetClientConfigResultOutput, *GetClientConfigResult](outputResult)
}

type GetClientConfigResultOutput struct{ *pulumi.OutputState }

func (GetClientConfigResultOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*GetClientConfigResult)(nil)).Elem()
}

func (o GetClientConfigResultOutput) ToOutput(context.Context) pulumix.Output[*GetClientConfigResult] {
	return pulumix.Output[*GetClientConfigResult]{
		OutputState: o.OutputState,
	}
}

func (o GetClientConfigResultOutput) ClientId() pulumix.Output[string] {
	return pulumix.Apply[*GetClientConfigResult](o, func(v *GetClientConfigResult) string { return v.ClientId })
}

func (o GetClientConfigResultOutput) ObjectId() pulumix.Output[string] {
	return pulumix.Apply[*GetClientConfigResult](o, func(v *GetClientConfigResult) string { return v.ObjectId })
}

func (o GetClientConfigResultOutput) SubscriptionId() pulumix.Output[string] {
	return pulumix.Apply[*GetClientConfigResult](o, func(v *GetClientConfigResult) string { return v.SubscriptionId })
}

func (o GetClientConfigResultOutput) TenantId() pulumix.Output[string] {
	return pulumix.Apply[*GetClientConfigResult](o, func(v *GetClientConfigResult) string { return v.TenantId })
}
